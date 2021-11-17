from django.views import View
from api.controllers.order_history_controller import get_order_detail
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class OrderDetailApiView(View):
    def get(self, request: HttpRequest, orderId: int) -> HttpResponse:
        return responseJson(get_order_detail(order_id=orderId))