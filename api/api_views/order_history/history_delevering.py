from django.views import View
from api.controllers.order_history_controller import get_delevering_order_history
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class DeleveringOrderHistoryApiView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_delevering_order_history(userId=1))