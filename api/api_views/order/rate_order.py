from django.views import View
from django.http import HttpRequest, HttpResponse
from django.http.response import Http404
import json
from django.utils.decorators import method_decorator
from api.network_models import RateOrderRequest
from django.views.decorators.csrf import csrf_exempt
from api.controllers.order_controller import rate_order

@method_decorator(csrf_exempt, name='dispatch')
class RateOrder(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        if request.method == "POST":
            body: dict = json.loads(request.body)
            rateOrderRequest : RateOrderRequest = RateOrderRequest(
                order_id= body["orderId"],
                driver_score= body["driverScore"],
                order_score= body["orderScore"]
            )
            status : bool = rate_order(rateOrderRequest)
            if status:
                return HttpResponse(status = 200)
            else:
                return HttpResponse(status = 400)
        else:
            raise Http404("Does not exist") 