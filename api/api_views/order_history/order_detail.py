from django.http.response import HttpResponseNotFound
from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.order_history_controller import get_order_detail
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class OrderDetailApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest, orderId: int) -> HttpResponse:
        user_id = self.get_jwt_user_id(request)
        order = get_order_detail(order_id=orderId, user_id= user_id)
        if order:
            return responseJson(order)
        else:
            return HttpResponseNotFound()