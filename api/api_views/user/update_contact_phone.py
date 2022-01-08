from django.utils.decorators import method_decorator
from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpRequest, HttpResponse
from api.network_models import PhoneNumberResponse
import json
from django.http.response import HttpResponseBadRequest
from api.controllers.user_controller import update_contact_phone
from api.util import responseJson


@method_decorator(csrf_exempt, name='dispatch')
class UpdateContactPhone(JwtLoginRequiredMixin, View):
    def post(self, request: HttpRequest) -> HttpResponse:
        user_id: int = self.get_jwt_user_id(request)
        body: dict = json.loads(request.body)
        result: PhoneNumberResponse = update_contact_phone(body["phone_number"], user_id)
        if result is None:
            return HttpResponseBadRequest()
        else:
            return responseJson(result)
