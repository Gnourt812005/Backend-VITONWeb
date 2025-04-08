from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_database
from app.crud.product_image import product_image_crud
from app.schemas.product_image import ProductImageCreate, ProductImageUpdate, ProductImageOut

router = APIRouter()

# GET: Fetch all data
@router.get("/", response_model=List[ProductImageOut])
async def get_all(db : Session = Depends(get_database)):
    return product_image_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/{id}", response_model=ProductImageOut)
async def get(id: int, db : Session = Depends(get_database)):
    response = product_image_crud.get(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Image not found")
    return response

# POST: Create new row
@router.post("/", response_model=ProductImageOut, status_code=status.HTTP_201_CREATED)
async def create(obj_in: ProductImageCreate, db: Session = Depends(get_database)):
    return product_image_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/{id}", response_model=ProductImageOut)
async def update(id: int, obj_in: ProductImageUpdate, db : Session = Depends(get_database)):
    db_obj = product_image_crud.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Image not found")
    return product_image_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/{id}", response_model=ProductImageOut)
async def delete(id: int, db : Session = Depends(get_database)):
    response = product_image_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Image not found")
    return response