from fastapi import FastAPI
from .api import router as stations_router
from . import constants

tags_metadata = constants.TAGS_METADATA
app = FastAPI(
    title="Space App",
    description="Simple API to space Stations",
    version="1.0.0",
    openapi_tags=tags_metadata
)
app.include_router(stations_router)


