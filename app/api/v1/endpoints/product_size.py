from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.database import get_database
from app.crud.product_size import product_size_crud
from app.schemas.product_size import ProductSizeCreate, ProductSizeUpdate, ProductSizeOut

router = APIRouter()

# GET: Fetch all data
@router.get("/", response_model=List[ProductSizeOut])
async def get_all(db : Session = Depends(get_database)):
    return product_size_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/{product_id}{size_id}", response_model=ProductSizeOut)
async def get(product_id: UUID, size_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "size_id": size_id}
    response = product_size_crud.get(db=db, keys=keys)
    if not response:
        raise HTTPException(status_code=404, detail="Product does not have this size")
    return response

# POST: Create new row
@router.post("/", response_model=ProductSizeOut, status_code=status.HTTP_201_CREATED)
async def create(obj_in: ProductSizeCreate, db: Session = Depends(get_database)):
    return product_size_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/{product_id}{size_id}", response_model=ProductSizeOut)
async def update(product_id: UUID, size_id: int, obj_in: ProductSizeUpdate, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "size_id": size_id}
    db_obj = product_size_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this size")
    return product_size_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/{product_id}{size_id}", response_model=ProductSizeOut)
async def delete(product_id: UUID, size_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "size_id": size_id}
    db_obj = product_size_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this size")
    return product_size_crud.delete(db=db, db_obj=db_obj)