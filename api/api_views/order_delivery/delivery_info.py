from django.http import Http404
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.util import responseJson
from django.views import View
from api.network_models import  OrderDeliveryInfo

from api.controllers.order_controller import order_delivery_infor
class DeliveryInfo(JwtLoginRequiredMixin ,View):
    def get(self, request: HttpRequest, orderId : int) -> HttpResponse:
        user_id : int = self.get_jwt_user_id(request)
        result : OrderDeliveryInfo = order_delivery_infor(orderId, user_id)
        if result is None:
            raise Http404("Does not exist") 
        else:
            return responseJson(result)
    