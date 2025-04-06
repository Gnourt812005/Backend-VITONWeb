from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_database
from app.crud.colors import colors_crud
from app.schemas.colors import ColorsCreate, ColorsUpdate, ColorsOut

router = APIRouter()

# GET: Fetch all data
@router.get("/colors", response_model=List[ColorsOut])
async def get_all(db : Session = Depends(get_database)):
    return colors_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/colors/{id}", response_model=ColorsOut)
async def get(id: int, db : Session = Depends(get_database)):
    response = colors_crud.get(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Color not found")
    return response

# POST: Create new row
@router.post("/colors", response_model=ColorsOut)
async def create(obj_in: ColorsCreate, db: Session = Depends(get_database)):
    return colors_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/colors/{id}", response_model=ColorsOut)
async def update(id: int, obj_in: ColorsUpdate, db : Session = Depends(get_database)):
    db_obj = colors_crud.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Color not found")
    return colors_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/colors/{id}", response_model=ColorsOut)
async def delete(id: int, db : Session = Depends(get_database)):
    response = colors_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Color not found")
    return response