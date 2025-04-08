from fastapi import APIRouter, Depends, HTTPException
from fastapi import status
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID

from app.core.database import get_database
from app.crud.product_color import product_color_crud
from app.schemas.product_color import ProductColorCreate, ProductColorUpdate, ProductColorOut

router = APIRouter()

# GET: Fetch all data
@router.get("/", response_model=List[ProductColorOut])
async def get_all(db : Session = Depends(get_database)):
    return product_color_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/{product_id}{color_id}", response_model=ProductColorOut)
async def get(product_id: UUID, color_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "color_id": color_id}
    response = product_color_crud.get(db=db, keys=keys)
    if not response:
        raise HTTPException(status_code=404, detail="Product does not have this color")
    return response

# POST: Create new row
@router.post("/", response_model=ProductColorOut, status_code=status.HTTP_201_CREATED)
async def create(obj_in: ProductColorCreate, db: Session = Depends(get_database)):
    return product_color_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/{product_id}{color_id}", response_model=ProductColorOut)
async def update(product_id: UUID, color_id: int, obj_in: ProductColorUpdate, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "color_id": color_id}
    db_obj = product_color_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this color")
    return product_color_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/{product_id}{color_id}", response_model=ProductColorOut)
async def delete(product_id: UUID, color_id: int, db : Session = Depends(get_database)):
    keys = {"product_id" : product_id, "color_id": color_id}
    db_obj = product_color_crud.get(db=db, keys=keys)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Product does not have this color")
    return product_color_crud.delete(db=db, db_obj=db_obj)