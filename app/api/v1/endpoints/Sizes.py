from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_database
from app.crud.sizes import sizes_crud
from app.schemas.sizes import SizesCreate, SizesUpdate, SizesOut

router = APIRouter()

# GET: Fetch all data
@router.get("/sizes", response_model=List[SizesOut])
async def get_all(db : Session = Depends(get_database)):
    return sizes_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/sizes/{id}", response_model=SizesOut)
async def get(id: int, db : Session = Depends(get_database)):
    response = sizes_crud.get(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Size not found")
    return response

# POST: Create new row
@router.post("/sizes", response_model=SizesOut)
async def create(obj_in: SizesCreate, db: Session = Depends(get_database)):
    return sizes_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/sizes/{id}", response_model=SizesOut)
async def update(id: int, obj_in: SizesUpdate, db : Session = Depends(get_database)):
    db_obj = sizes_crud.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Size not found")
    return sizes_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/sizes/{id}", response_model=SizesOut)
async def delete(id: int, db : Session = Depends(get_database)):
    response = sizes_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Size not found")
    return response