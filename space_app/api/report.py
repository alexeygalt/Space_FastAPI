from fastapi import APIRouter, UploadFile, File, Depends
from starlette.background import BackgroundTasks
from starlette.responses import StreamingResponse

from space_app.services.report import ReportService

router = APIRouter(
    prefix='/reports',
    tags=['Reports']
)


@router.post('/import')
def import_csv(
        background_tasks: BackgroundTasks,
        file: UploadFile = File(...),
        reports_service: ReportService = Depends(),

):
    """
    Import Stations(name: str)  from .csv to DB
    \f
    :param background_tasks:
    :param file:
    :param reports_service:
    :return:
    """
    background_tasks.add_task(
        reports_service.import_csv,
        file.file
    )


@router.post('/export')
def export_csv(
        reports_service: ReportService = Depends()
):
    """
    Export all Stations to .csv
    \f
    :param reports_service:
    :return:
    """
    report = reports_service.export_csv()
    return StreamingResponse(
        report,
        media_type='text/csv',
        headers={
            'Content-Disposition': 'attachment; filename=report.csv'
        },
    )
