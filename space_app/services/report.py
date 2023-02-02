import csv
from io import StringIO
from typing import Any

from fastapi import Depends

from space_app.schemas.station import CreateStation, FullStation
from space_app.services.station_service import StationService


class ReportService:
    def __init__(self, station_service: StationService = Depends()):
        self.station_service = station_service

    def import_csv(self, file: Any):
        reader = csv.DictReader(
            (line.decode() for line in file),
            fieldnames=[
                'name',
            ],
            # extrasaction='ignore',
        )
        stations = []
        next(reader)

        for row in reader:
            station_data = CreateStation.parse_obj(row)
            stations.append(station_data)
        self.station_service.create_many_stations(station_data=stations)

    def export_csv(self) -> Any:
        output = StringIO()
        writer = csv.DictWriter(
            output,
            fieldnames=[
                'name',
                'condition',
                'date_created',
                'date_broken',
                'x',
                'y',
                'z',
            ],
            extrasaction='ignore',
        )
        stations = self.station_service.get_all_station()
        writer.writeheader()
        for station in stations:
            station_data = FullStation.from_orm(station)
            writer.writerow(station_data.dict())
        output.seek(0)
        return output
