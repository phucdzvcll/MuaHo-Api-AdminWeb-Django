from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from api.auth.jwt_helper import decode_jwt_token, encode_jwt_token
from api.auth.jwt_user import HttpResponseAuthError
from api.controllers.user_controller import  RefreshTokenResult, refresh_token
from api.network_models import RefreshTokenNw
from api.util import responseJson

@method_decorator(csrf_exempt, name='dispatch')
class RefreshTokenView(View):
    def post(self, request: HttpRequest) -> HttpResponse:    
        refreshToken: str = json.loads(request.body)["refresh_token"]
        result : RefreshTokenResult = refresh_token(refreshToken)
        if result.token:
            return responseJson(result.token)
        elif result.isExpire:
            return HttpResponseAuthError()
        else:
            return HttpResponseBadRequest()