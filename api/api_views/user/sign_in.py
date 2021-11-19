from django.http.request import HttpRequest
from django.http.response import Http404, HttpResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json
from django.utils.decorators import method_decorator
from api.controllers.sign_in_controller import sign_in


from api.util import responseJson

@method_decorator(csrf_exempt, name='dispatch')
class SignInView(View):
    def post(self, request: HttpRequest) -> HttpResponse:    
        firebaseToken: str = json.loads(request.body)["firebase_token"]
        result = sign_in(firebaseToken)
        if result:
            return responseJson(result)
        else:
            return HttpResponse(status = 400)
        
        
        
