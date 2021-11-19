from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.util import responseJson
from api.controllers.search_controller import search_shop

class SearchShop(JwtLoginRequiredMixin ,View):
    def get(self, request: HttpRequest) -> HttpResponse:
        queryParam : str = request.GET.get('keyword', '')
        return responseJson(search_shop(queryParam))