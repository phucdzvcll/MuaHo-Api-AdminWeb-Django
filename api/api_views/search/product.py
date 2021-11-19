from django.views import View
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from api.network_models import ShopProducts
from api.controllers.search_controller import shop_product
from django.http import Http404

class SearchProduct(View):
    def get(self, request: HttpRequest, shopID : int) -> HttpResponse:
        if request.method == "GET":
            shop_product_result : ShopProducts = shop_product(shopID)
            if shop_product_result is None:
                raise Http404("Does not exist")
            else:
                return responseJson(shop_product_result)
        else:    
            raise Http404("Does not exist") 