from django.views import View
from django.http import HttpRequest, HttpResponse
from django.http.response import HttpResponseBadRequest
import json
from django.utils.decorators import method_decorator
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.network_models import RateOrderRequest
from django.views.decorators.csrf import csrf_exempt
from api.controllers.order_controller import rate_order


@method_decorator(csrf_exempt, name='dispatch')
class RateOrder(JwtLoginRequiredMixin ,View):
    def post(self, request: HttpRequest) -> HttpResponse:
        user_id : int = self.get_jwt_user_id(request)
        body: dict = json.loads(request.body)
        rateOrderRequest : RateOrderRequest = RateOrderRequest(
            order_id= body["orderId"],
            driver_score= body["driverScore"],
            order_score= body["orderScore"]
        )
        status : bool = rate_order(rateOrderRequest, user_id)
        if status:
            return HttpResponse()
        else:
            return HttpResponseBadRequest()