
import datetime
from math import ceil
from api.models import APIConfig
import json
from datetime import datetime

class MaintenanceStatus:
    def __init__(self, status: bool, total_minutes: int):
        self.status = status
        self.totalMinutes = total_minutes


def getMaintenanceStatus() -> MaintenanceStatus:
    try:
        config: APIConfig = APIConfig.objects.get(id='maintenance')
        status: bool = config.status
        if status:
            value: str = config.value
            dictValue: dict = json.loads(value)
            maintenanceStatus: bool = dictValue["status"]
            finishDateTimeUtc: str = dictValue["finish_date_time_utc"]
            dateTime: datetime.datetime = datetime.strptime(
                finishDateTimeUtc, '%Y-%m-%d %H:%M:%S')
            detltaTime: datetime.timedelta = dateTime - datetime.utcnow()
            totalMinutes: int
            if detltaTime.days < 0:
                totalMinutes = 0
            else:
                totalMinutes: int = ceil(detltaTime.seconds / 60)
            return MaintenanceStatus(status=maintenanceStatus, total_minutes=totalMinutes)
        else:
            return MaintenanceStatus(status=False, total_minutes=0)
    except Exception as e:
        return MaintenanceStatus(status=False, total_minutes=0)
