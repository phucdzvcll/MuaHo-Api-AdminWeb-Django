from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.util import responseJson
from api.controllers.search_controller import get_hot_shop

class GetHotSearch(JwtLoginRequiredMixin ,View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_hot_shop())