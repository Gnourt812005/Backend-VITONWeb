import logging

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# 
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import and_
from typing import List, Optional
from uuid import UUID

# DB, Cached client
from app.core.database import get_database
# from app.services.redis_service import RedisService, get_redis_service
from app.crud.products import products_crud

# model of each tables use for query ORM
from app.models.product_color import ProductColor
from app.models.product_size import ProductSize
from app.models.product_tag import ProductTag
from app.models.product_size import ProductSize
from app.models.product_image import ProductImage
from app.models.products import Products
from app.models.colors import Colors
from app.models.tags import Tags
from app.models.sizes import Sizes

# Schema for input, output of API
from app.schemas.products import ProductsCreate, ProductsUpdate, ProductsOut
import time
logger = logging.getLogger(__name__)
router = APIRouter()

def serialize_product_size(obj):
    res = []

    for item in obj:
        extract = {
            "size_code" : None,
            "display_name" : None,
            "available" : None 
        }
        try:
            extract["size_code"] = item.rlts_sizes.size_code if item.rlts_sizes else None
            extract["display_name"] = item.rlts_sizes.display_name if item.rlts_sizes else None
            extract["available"] = item.available
        except Exception as e:
            print(e)
        finally:
            res.append(extract)
    return {"sizes" : res}

def serialize_product_color(obj):
    res = []

    for item in obj:
        extract = {
            "hex_code" : None,
            "color_name" : None,
            "available" : None 
        }
        try:
            extract["hex_code"] = item.rlts_colors.hex_code if item.rlts_colors else None
            extract["color_name"] = item.rlts_colors.color_name if item.rlts_colors else None
            extract["available"] = item.available
        except Exception as e:
            print(e)
        finally:
            res.append(extract)
    return {"colors" :  res}

def serialize_product_tag(obj):
    res = []

    for item in obj:
        extract = ""
        try:
            extract = item.rlts_tags.tag_name if item.rlts_tags else None
        except Exception as e:
            print(e)
        finally:
            res.append(extract)
    return {"tags" : res}

def serialize_product_image(obj):
    res = {
        "imageUrl" : None,
        "images" : []
    }
    for item in obj:
        try:
            if item.is_primary == True:
                res["imageUrl"] = item.image_url
            else:
                res["images"].append({"url" : item.image_url, "alt" : item.alt_text})
        except Exception as e:
            print(f"Error: {e}")
        finally:
            pass 
    return res


@router.get("/products", response_model=List[ProductsOut], response_model_exclude_unset=True)
async def get_all(
        fields : Optional[str] = Query(None, description="Comma-separated list of fields to include"),
        page : Optional[int] = Query(1, description="page index"),
        db : Session = Depends(get_database), 
        ):
    start = time.time()
    data_products = (db.query(
                        Products,
                        ProductImage.image_url.label("imageUrl")
                    ).select_from(Products)
                    .join(ProductImage, Products.id == ProductImage.product_id)
                    .filter(ProductImage.is_primary == True)
                    .limit(10)
                    .offset(10 * (page - 1))
                    .all())
    logger.info(f"Fetch data completed in {(time.time() - start):2f}s")
    # Serialize response
    response = []
    for product, url in data_products:
        serialized_product = jsonable_encoder(product)
        serialized_product["imageUrl"] = url 
        response.append(serialized_product)

    # Filter requested fields
    if fields:
        requested_fields = set(fields.split(','))
        response = [
            {key: value for key, value in product.items() if key in requested_fields}
            for product in response
        ]
    return response

@router.get("/product/{id}", response_model=ProductsOut, response_model_exclude_unset=True)
async def get(
        id: UUID,
        fields : Optional[str] = Query(None, description="Comma-separated list of fields to include"), 
        db : Session = Depends(get_database)
        ):
    # Fetch database
    start = time.time()
    data_product = products_crud.get(db=db, id=id)
    if not data_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Fetch relative fields 
    data_product = jsonable_encoder(data_product)

    data = (
        db.query(
            Colors.hex_code.label("hex_code"),
            Colors.color_name.label("color_name"),
            ProductColor.available.label("color_available"),
            Sizes.size_code.label("size_code"),
            Sizes.display_name.label("display_name"),
            ProductSize.available.label("size_available"),
            Tags.tag_name.label("tag_name"),
            ProductImage.image_url.label("image_url"), 
            ProductImage.alt_text.label("alt_text"), 
            ProductImage.is_primary.label("is_primary")
        )
        .select_from(Products)
        .outerjoin(ProductColor, Products.id == ProductColor.product_id)
        .outerjoin(Colors, ProductColor.color_id == Colors.id)
        .outerjoin(ProductSize, Products.id == ProductSize.product_id)
        .outerjoin(Sizes, ProductSize.size_id == Sizes.id)
        .outerjoin(ProductTag, Products.id == ProductTag.product_id)
        .outerjoin(Tags, ProductTag.tag_id == Tags.id)
        .outerjoin(ProductImage, ProductImage.product_id == Products.id)
        .filter(Products.id == id)
        .all()
    )
    colors = []
    sizes = []
    tags = []
    images = []
    imageUrl = ""
    for row in data:
        # Add unique colors
        if row.hex_code and row.color_name:
            color = {"hex_code": row.hex_code, "color_name": row.color_name, "available": row.color_available}
            if color not in colors:
                colors.append(color)

        # Add unique sizes
        if row.size_code and row.display_name:
            size = {"size_code": row.size_code, "display_name": row.display_name, "available": row.size_available}
            if size not in sizes:
                sizes.append(size)

        # Add unique tags
        if row.tag_name:
            tag = {"tag_name": row.tag_name}
            if tag not in tags:
                tags.append(tag)

        # Add unique images
        if row.image_url:
            if row.is_primary:
                imageUrl = row.image_url
                continue
            image = {"url": row.image_url, "alt": row.alt_text}
            if image not in images:
                images.append(image)

    logger.info(f"Fetch data completed in {(time.time() - start):2f}s")

    response = {
        **data_product,
        "colors": colors,
        "sizes": sizes,
        "tags": tags,
        "images": images,
        "imageUrl" : imageUrl
    }
    # Filter fields
    if fields:
        requested_fields = set(fields.split(','))
        response = {
            key: value for key, value in response.items() if key in requested_fields
        }

    return response