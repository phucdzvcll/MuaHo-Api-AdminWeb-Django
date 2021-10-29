from api.controllers.home_controller import get_categories
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from api.controllers import *

def categories(request: HttpRequest) -> HttpResponse:
    return responseJson(get_categories())
