from api.controllers.home_controller import get_categories
from api.controllers.order_history_controller import get_complete_order_history, get_delevering_order_history
from api.controllers.search_controller import get_hot_shop
from api.controllers.search_controller import search_shop
from api.controllers.search_controller import shop_product
from api.controllers.home_controller import get_banners, get_categories
from django.http import HttpRequest, HttpResponse
from api.controllers.voucher_controller import get_list_voucher
from api.util import responseJson
from api.controllers import *
from django.http import Http404

def categories(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_categories())
    else:    
        raise Http404("Does not exist")

def banners(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_banners())
    else:    
        raise Http404("Does not exist")

def getListVoucher(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_list_voucher(1))
    else:    
        raise Http404("Does not exist")

def getHotSearch(request: HttpRequest) -> HttpResponse:
    return responseJson(get_hot_shop())

def searchShop(request: HttpRequest) -> HttpResponse:
    queryParam : str = request.GET.get('keyword', '')
    return responseJson(search_shop(queryParam))

def products(request: HttpRequest, shopID : int) -> HttpResponse:
    return responseJson(shop_product(shopID))


def getOrderHistoryDelivering(request: HttpRequest) -> HttpResponse:
    return responseJson(get_delevering_order_history(userId=1))

def getOrderHistoryComplete(request: HttpRequest) -> HttpResponse:
    return responseJson(get_complete_order_history(userId=1))