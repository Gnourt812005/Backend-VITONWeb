from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.database import get_database
from app.crud.ProductTag import product_tag_crud
from app.schemas.ProductTag import ProductTagCreate, ProductTagUpdate, ProductTagOut

router = APIRouter()

# GET: Fetch all data
@router.get("/product_tag", response_model=List[ProductTagOut])
async def get_all(db : Session = Depends(get_database)):
    return product_tag_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/product_tag/{product_id}{tag_id}", response_model=ProductTagOut)
async def get(product_id: UUID, tag_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "tag_id": tag_id}
    response = product_tag_crud.get(db=db, keys=keys)
    if not response:
        raise HTTPException(status_code=404, detail="Product does not have this tag")
    return response

# POST: Create new row
@router.post("/product_tag", response_model=ProductTagOut)
async def create(obj_in: ProductTagCreate, db: Session = Depends(get_database)):
    return product_tag_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/product_tag/{product_id}{tag_id}", response_model=ProductTagOut)
async def update(product_id: UUID, tag_id: int, obj_in: ProductTagUpdate, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "tag_id": tag_id}
    db_obj = product_tag_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this tag")
    return product_tag_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/product_tag/{product_id}{tag_id}", response_model=ProductTagOut)
async def delete(product_id: UUID, tag_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "tag_id": tag_id}
    db_obj = product_tag_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this tag")
    return product_tag_crud.delete(db=db, db_obj=db_obj)