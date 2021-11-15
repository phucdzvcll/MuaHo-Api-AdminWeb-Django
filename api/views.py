from api.controllers.search_controller import get_hot_shop
from api.controllers.search_controller import search_shop
from api.controllers.search_controller import shop_product
from django.http import HttpRequest, HttpResponse

from api.util import responseJson
from api.controllers import *

def getHotSearch(request: HttpRequest) -> HttpResponse:
    return responseJson(get_hot_shop())

def searchShop(request: HttpRequest) -> HttpResponse:
    queryParam : str = request.GET.get('keyword', '')
    return responseJson(search_shop(queryParam))

def products(request: HttpRequest, shopID : int) -> HttpResponse:
    return responseJson(shop_product(shopID))