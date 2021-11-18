from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.home_controller import get_categories
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class CategoryApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_categories())