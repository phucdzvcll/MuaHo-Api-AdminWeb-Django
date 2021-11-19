from django.views import View
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from api.controllers.search_controller import get_hot_shop

class GetHotSearch(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_hot_shop())