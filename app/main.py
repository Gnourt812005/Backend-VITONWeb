from fastapi                            import FastAPI, Request
from contextlib                         import asynccontextmanager
from app.core.config                    import settings
from app.core.database                  import engine, Base
from app.core.logger                    import setup_logger
import logging
import time

from app.api.v1 import router_v1
from app.api.v2 import router_v2
from app.api.v3 import router_v3
from app.api.v4 import router_v4
from fastapi.middleware.cors import CORSMiddleware
# Startup and shutdown event

setup_logger()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app : FastAPI):
    try: 
        with engine.connect() as connection:
            logger.info("Database connect successfully")
        # Base.metadata.create_all(bind=engine)
    except Exception as e:
        logger.error(f"Database connection failed: {e}")
    yield
    # Base.metadata.drop_all(bind=engine)

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)

origins = [
    "http://localhost:3000",  # Your Next.js frontend
    # You can add more origins here, e.g., "https://your-production-domain.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,           # Allows requests from the specified origins
    allow_credentials=True,          # Allows cookies and credentials
    allow_methods=["*"],             # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],             # Allows all headers
)

@app.middleware("http")
async def log_request(request : Request, call_next):
    start = time.time()
    response = await call_next(request)

    logger.info(f"{request.method} completed in {(time.time() - start):2f}s")
    return response

# Config routing
app.include_router(router_v4, prefix="/api/v4")

# Test 
@app.get("/test")
async def test():
    logger.info("Test endpoint hit!")
    return {"msg": "Hello!"}

