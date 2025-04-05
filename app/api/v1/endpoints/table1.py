from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse

from app.core.database import get_database
from sqlalchemy.orm import Session
from app.models.table1 import ImagePerson

router = APIRouter()



@router.get("/imageperson")
async def getProductImages(db : Session = Depends(get_database) ):
    try:
        response = db.query(ImagePerson).all()
        data = [{"id": image.id, "url": image.url, "created_at" : image.created_at.isoformat()} for image in response]
        return JSONResponse(content=data)
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": "An error occurred"}, status_code=500)
    
@router.get("/imageperson/{id}")
async def getProductImages(id : int, db : Session = Depends(get_database) ):
    try:
        response = db.query(ImagePerson).filter(ImagePerson.id == id)
        data = [{"id": image.id, "url": image.url} for image in response]
        return JSONResponse(content=data)
    except Exception as e:
        print(f"Error: {e}")
        return JSONResponse(content={"error": "An error occurred"}, status_code=500)

