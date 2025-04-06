from fastapi import APIRouter
from pathlib import Path
import importlib
import pkgutil

router_v1 = APIRouter()

package_dir = Path(__file__).resolve().parent / "endpoints"
for _, module_name, _ in pkgutil.iter_modules([str(package_dir)]):
    module = importlib.import_module(f"app.api.v1.endpoints.{module_name}")
    if hasattr(module, "router"):
        router_v1.include_router(module.router, prefix=f"/{module_name}", tags=[module_name])