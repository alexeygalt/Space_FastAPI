from fastapi import APIRouter
from .stations import router as stations_router
from .indications import router as indication_router
from .state import router as state_indication
from .auth import router as auth_router
from .report import router as report_router
router = APIRouter()

router.include_router(stations_router)
router.include_router(indication_router)
router.include_router(state_indication)
router.include_router(auth_router)
router.include_router(report_router)


