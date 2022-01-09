from django.http import HttpResponse

from api.controllers.api_config_controller import getMaintenanceStatus, MaintenanceStatus
from api.network_models import MaintenanceResponse
from api.util import toJson


class HttpResponseMaintenance(HttpResponse):
    status_code = 999


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        if request.path.startswith('/api/'):

            maintenance: MaintenanceStatus = getMaintenanceStatus()
            if maintenance.status:
                maintenanceResponse: MaintenanceResponse = MaintenanceResponse(
                    totalMinutes=maintenance.totalMinutes)
                return HttpResponseMaintenance(toJson(maintenanceResponse), content_type="application/json")
            else:
                return self.get_response(request)
        else:
            return self.get_response(request)
