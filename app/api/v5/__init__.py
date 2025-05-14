from fastapi import APIRouter, Depends 
from pathlib import Path
import importlib
import pkgutil
from app.services.redis_service import get_redis_service 

router_v5 = APIRouter(dependencies=[Depends(get_redis_service)])

package_dir = Path(__file__).resolve().parent / "endpoints"
for _, module_name, _ in pkgutil.iter_modules([str(package_dir)]):
    module = importlib.import_module(f"app.api.v5.endpoints.{module_name}")
    if hasattr(module, "router"):
        router_v5.include_router(module.router, tags=[module_name])