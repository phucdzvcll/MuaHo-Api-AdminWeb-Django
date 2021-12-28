from django.http.response import HttpResponseBadRequest
from django.utils.decorators import method_decorator
from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.address_controller import create_user_address, get_list_address
from django.http import HttpRequest, HttpResponse
from api.network_models import CreateUserAddressRequest
from api.util import responseJson
from django.views.decorators.csrf import csrf_exempt
import json

def mapCreateOrderRequest(dictCreateAddress : dict) -> CreateUserAddressRequest:
    return CreateUserAddressRequest(
        address=dictCreateAddress["address"],
        contact_phone_number=dictCreateAddress["contact_phone_number"],
        lat=dictCreateAddress["lat"],
        lng=dictCreateAddress["lng"],
    )

@method_decorator(csrf_exempt, name='dispatch')
class AddressApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = self.get_jwt_user_id(request)
        return responseJson(get_list_address(user_id=user_id))

    def post(self, request: HttpRequest) -> HttpResponse:
        body : dict = json.loads(request.body)
        user_id : int = self.get_jwt_user_id(request)
        status = create_user_address(user_id=user_id, address=mapCreateOrderRequest(body))
        if status:
            return HttpResponse()
        else:
            return HttpResponseBadRequest()
        