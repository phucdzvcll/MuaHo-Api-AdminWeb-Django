from django.http import Http404
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from django.views import View
from api.network_models import  OrderDeliveryInfo

from api.controllers.order_controller import order_delivery_infor
class DeliveryInfo(View):
    def get(self, request: HttpRequest, orderId : int) -> HttpResponse:
        if request.method == "GET":
            result : OrderDeliveryInfo = order_delivery_infor(orderId)
            if result is None:
                raise Http404("Does not exist") 
            else:
                return responseJson(result)
        else:    
            raise Http404("Does not exist") 