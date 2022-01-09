from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.api_config_controller import MaintenanceStatus, getMaintenanceStatus
from api.network_models import CheckMantenanceResponse
from api.util import responseJson

class MaintenanceStatusView(JwtLoginRequiredMixin ,View):
    def get(self, request: HttpRequest) -> HttpResponse:
        maintenance: MaintenanceStatus = getMaintenanceStatus()
        checkMantenanceResponse : CheckMantenanceResponse = CheckMantenanceResponse(maintenanceStatus = maintenance.status)
        return responseJson(checkMantenanceResponse)