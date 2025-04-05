from sqlalchemy.orm import Session 
from typing import Type, TypeVar, Optional, Generic, List, Dict
from pydantic import BaseModel

ModelType = TypeVar("ModelType")
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

class BaseCRUDComposite (Generic[ModelType, CreateSchemaType, UpdateSchemaType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model 
    
    def get_all(self, db: Session) -> List[ModelType]:
        return db.query(self.model).all()
    
    def get(self, db: Session, keys: Dict[str, any]) -> Optional[ModelType]:
        data = db.query(self.model)
        for key, value in keys.items():
            data = data.filter(getattr(self.model, key) == value)
        return data.first()

    def create(self, db: Session, obj_in: CreateSchemaType) -> Optional[ModelType]:
        obj = self.model(**obj_in.model_dump())
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def update(self, db: Session, db_obj: ModelType, obj_in: UpdateSchemaType) -> Optional[ModelType]:
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        db.commit()
        db.refresh(db_obj)
        return db_obj 

    def delete(self, db: Session, db_obj: ModelType) -> Optional[ModelType]:
        # obj = self.get(db, keys)
        if db_obj:
            db.delete(db_obj)
            db.commit()
        return db_obj

