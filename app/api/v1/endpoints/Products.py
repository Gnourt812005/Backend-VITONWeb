from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.database import get_database
from app.crud.Products import products_crud
from app.schemas.Products import ProductsCreate, ProductsUpdate, ProductsOut

router = APIRouter()

# GET: Fetch all data
@router.get("/products", response_model=List[ProductsOut])
async def get_all(db : Session = Depends(get_database)):
    return products_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/product/{id}", response_model=ProductsOut)
async def get(id: UUID, db : Session = Depends(get_database)):
    response = products_crud.get(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Product not found")
    return response

# POST: Create new row
@router.post("/products", response_model=ProductsOut)
async def create(obj_in: ProductsCreate, db: Session = Depends(get_database)):
    return products_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/product/{id}", response_model=ProductsOut)
async def update(id: UUID, obj_in: ProductsUpdate, db : Session = Depends(get_database)):
    db_obj = products_crud.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product not found")
    return products_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/product/{id}", response_model=List[ProductsOut])
async def delete(id: UUID, db : Session = Depends(get_database)):
    response = products_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Product not found")
    return response