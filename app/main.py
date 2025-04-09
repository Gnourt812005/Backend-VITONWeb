from fastapi                            import FastAPI
from contextlib                         import asynccontextmanager
from app.core.config                    import settings
from app.core.database                  import engine, Base

# from app.api.v1.endpoints.Products      import router as products_router
# from app.api.v1.endpoints.Sizes         import router as sizes_router
# from app.api.v1.endpoints.Tags          import router as tags_router
# from app.api.v1.endpoints.Colors        import router as colors_router
# from app.api.v1.endpoints.ProductImage  import router as product_image_router
# from app.api.v1.endpoints.ProductColor  import router as product_color_router
# from app.api.v1.endpoints.ProductSize   import router as product_size_router
# from app.api.v1.endpoints.ProductTag    import router as product_tag_router
from sqlalchemy                         import inspect

from app.api.v1 import router_v1
from app.api.v2 import router_v2
# Startup and shutdown event
@asynccontextmanager
async def lifespan(app : FastAPI):
    try: 
        with engine.connect() as connection:
            print("Database coonect successfully")
        # Base.metadata.create_all(bind=engine)
    except Exception as e:
        print(f"Database connection failed: {e}")
    yield

app = FastAPI(
    title=settings.PROJECT_NAME,
    lifespan=lifespan
)


# Config routing
# app.include_router(products_router, prefix="/products", tags=["products"])
# app.include_router(sizes_router, prefix="/sizes", tags=["sizes"])
# app.include_router(colors_router, prefix="/colors", tags=["colors"])
# app.include_router(tags_router, prefix="/tags", tags=["tags"])
# app.include_router(product_image_router, prefix="/product_image", tags=["product_image"])
# app.include_router(product_color_router, prefix="/product_color", tags=["product_color"])
# app.include_router(product_size_router, prefix="/product_size", tags=["product_size"])
# app.include_router(product_tag_router, prefix="/product_tag", tags=["product_tag"])
app.include_router(router_v1, prefix="/api/v1")
app.include_router(router_v2, prefix="/api/v2")
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

# @app.post("/redis")
# async def create():
#     success = redis_engine.flushall()
#     return {"status" : success}

# @app.get("/redis")
# async def get(key : str):
#     # success = redis_engine.set('foo', 'bar')
#     return {redis_engine.ttl(key)}

