from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_database
from app.crud.tags import tags_crud
from app.schemas.tags import TagsCreate, TagsUpdate, TagsOut

router = APIRouter()

# GET: Fetch all data
@router.get("/", response_model=List[TagsOut])
async def get_all(db : Session = Depends(get_database)):
    return tags_crud.get_all(db=db)

# GET: Fetch with id
@router.get("/{id}", response_model=TagsOut)
async def get(id: int, db : Session = Depends(get_database)):
    response = tags_crud.get(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Tag not found")
    return response

# POST: Create new row
@router.post("/", response_model=TagsOut, status_code=status.HTTP_201_CREATED)
async def create(obj_in: TagsCreate, db: Session = Depends(get_database)):
    return tags_crud.create(db=db, obj_in=obj_in)

# PUT: Update row
@router.put("/{id}", response_model=TagsOut)
async def update(id: int, obj_in: TagsUpdate, db : Session = Depends(get_database)):
    db_obj = tags_crud.get(db=db, id=id)
    if not db_obj:
        raise HTTPException(status_code=404, detail="Tag not found")
    return tags_crud.update(db=db, db_obj=db_obj, obj_in=obj_in)

# DELETE: Delete row
@router.delete("/{id}", response_model=TagsOut)
async def delete(id: int, db : Session = Depends(get_database)):
    response = tags_crud.delete(db=db, id=id)
    if not response:
        raise HTTPException(status_code=404, detail="Tag not found")
    return response