from django.views import View
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from api.controllers.order_history_controller import  get_complete_order_history

class GetOrderHistoryComplete(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_complete_order_history(userId=1)) 