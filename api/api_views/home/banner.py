from django.views import View
from api.controllers.home_controller import get_banners
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class BannerApiView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_banners())