from fastapi import FastAPI
from fastapi.responses import JSONResponse
from contextlib import asynccontextmanager

import databases
from dotenv import load_dotenv
import os 

# Add file .env to get URL database
load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

database = databases.Database(DATABASE_URL)

# Startup and shutdown event
@asynccontextmanager
async def lifespan(app : FastAPI):
    await database.connect()
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)



@app.get("/imageperson")
async def getProductImages():
    try:
        query = "SELECT * FROM imageperson"
        response = await database.fetch_all(query)
        return JSONResponse(content=[dict(r) for r in response])
    except Exception as e:
        print("Error")

@app.get("/test")
async def test():
    print("Test endpoint hit!")
    return {"msg": "Hello!"}



