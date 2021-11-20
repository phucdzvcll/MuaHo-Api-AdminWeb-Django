from django.http.response import HttpResponseNotFound
from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.util import responseJson
from api.network_models import ShopProducts
from api.controllers.search_controller import shop_product

class SearchProduct(JwtLoginRequiredMixin ,View):
    def get(self, request: HttpRequest, shopID : int) -> HttpResponse:
        shop_product_result : ShopProducts = shop_product(shopID)
        if shop_product_result is None:
            return HttpResponseNotFound()
        else:
            return responseJson(shop_product_result)