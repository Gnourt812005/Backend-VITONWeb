from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.core.config import settings
from app.core.database import engine, Base

from app.api.v1.endpoints.table1 import router as table1_router

# Startup and shutdown event
@asynccontextmanager
async def lifespan(app : FastAPI):
    try: 
        with engine.connect() as connection:
            print("Database coonect successfully")
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database connection failed: {e}")
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)


# Config routing
app.include_router(table1_router, prefix="/table1", tags=["table1"])

# Test 
@app.get("/test")
async def test():
    print("Test endpoint hit!")
    return {"msg": "Hello!"}