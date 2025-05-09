import logging

from fastapi import APIRouter, Depends, HTTPException, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

# 
from sqlalchemy.orm import Session, joinedload
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

# Schema for input, output of API
from app.schemas.products import ProductsCreate, ProductsUpdate, ProductsOut

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
        db : Session = Depends(get_database), 
        ):
    data_products = (db.query(
                        Products,
                        ProductImage.image_url.label("imageUrl")
                    ).select_from(Products)
                    .join(ProductImage, Products.id == ProductImage.product_id)
                    .filter(ProductImage.is_primary == True).all())

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

# GET: Fetch with id
@router.get("/product/{id}", response_model=ProductsOut, response_model_exclude_unset=True)
async def get(
        id: UUID,
        fields : Optional[str] = Query(None, description="Comma-separated list of fields to include"), 
        db : Session = Depends(get_database)
        ):
    # Fetch database
    data_product = products_crud.get(db=db, id=id)
    if not data_product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    # Fetch relative fields 
    data_product = jsonable_encoder(data_product)
    data_colors = db.query(ProductColor).options(joinedload(ProductColor.rlts_colors)).filter(ProductColor.product_id==id).all()
    data_sizes = db.query(ProductSize).options(joinedload(ProductSize.rlts_sizes)).filter(ProductSize.product_id==id).all()
    data_tags = db.query(ProductTag).options(joinedload(ProductTag.rlts_tags)).filter(ProductTag.product_id==id).all()
    data_images = db.query(ProductImage).filter(ProductImage.product_id==id).all()

    # Serialize and aggregate to response
    response = {
        **data_product,
        **serialize_product_color(data_colors),
        **serialize_product_size((data_sizes)),
        **serialize_product_tag(data_tags),
        **serialize_product_image(data_images)
    }

    # Filter fields
    if fields:
        requested_fields = set(fields.split(','))
        response = {
            key: value for key, value in response.items() if key in requested_fields
        }

    return response

# # POST: Create new row
# @router.post("/product/", response_model=ProductsOut, status_code=status.HTTP_201_CREATED)
# async def create(obj_in: ProductsCreate, db: Session = Depends(get_database)):
#     return products_crud.create(db=db, obj_in=obj_in)

# # PUT: Update row
# @router.put("/product/{id}", response_model=ProductsOut)
# async def update(id: UUID, obj_in: ProductsUpdate, db : Session = Depends(get_database)):
#     db_obj = products_crud.get(db=db, id=id)
#     if not db_obj:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return products_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# # DELETE: Delete row
# @router.delete("/product/{id}", response_model=ProductsOut)
# async def delete(id: UUID, db : Session = Depends(get_database)):
    response = products_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Product not found")
    return response