from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import engine, Base

from app.api.v1.endpoints.table1 import router as table1_router
from app.api.v1.endpoints.Products import router as Products_router

from sqlalchemy import inspect
# Startup and shutdown event
@asynccontextmanager
async def lifespan(app : FastAPI):
    try: 
        with engine.connect() as connection:
            print("Database coonect successfully")
        print(settings.DATABASE_URL)
        # Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database connection failed: {e}")
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)


# Config routing
# app.include_router(table1_router, prefix="/table1", tags=["table1"])
app.include_router(Products_router, prefix="/products", tags=["products"])

# Test 
@app.get("/test")
async def test():
    print("Test endpoint hit!")
    return {"msg": "Hello!"}

@app.get("/tables/count")
async def get_table_count():
    inspector = inspect(engine)
    tables = inspector.get_table_names()
    return {"table_count": len(tables), "tables": tables}