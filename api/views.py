from django.http.response import HttpResponseBase
from api.controllers.home_controller import get_categories
from api.controllers.order_history_controller import get_complete_order_history, get_delevering_order_history
from api.controllers.search_controller import get_hot_shop
from api.controllers.search_controller import search_shop
from api.controllers.search_controller import shop_product
from api.controllers.home_controller import get_banners, get_categories
from api.controllers.order_controller import create_order, rate_order
from api.network_models import CreateOrderProduct, CreateOrderRequest, RateOrderRequest
from django.http import HttpRequest, HttpResponse
from api.controllers.voucher_controller import get_list_voucher
from api.network_models import ShopProducts
from api.util import responseJson
from api.controllers import *
from django.http import Http404
from django.db import transaction
from django.views.decorators.csrf import csrf_exempt
import json

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
    if request.method == "GET":
        shop_product_result : ShopProducts = shop_product(shopID)
        if shop_product_result is None:
            raise Http404("Does not exist")
        else:
            return responseJson(shop_product_result)
    else:    
        raise Http404("Does not exist") 

@csrf_exempt
def createOrder(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        try:
            with transaction.atomic():
                body : dict = json.loads(request.body)
                createOrderRequestObj : CreateOrderProduct = mapCreateOrderRequest(body)
                return responseJson(create_order(createOrderRequestObj))
        except Exception as e:
            print(str(e))
            raise Http404("Does not exist") 
    else:
        raise Http404("Does not exist") 

def mapCreateOrderRequest(dictCreateOrder : dict) -> CreateOrderRequest:
    print(dictCreateOrder)
    return CreateOrderRequest(
        voucher_id= dictCreateOrder["voucherId"],
        total_before_discount= dictCreateOrder["totalBeforeDiscount"],
        voucher_discount= dictCreateOrder["voucherDiscount"],
        total= dictCreateOrder["total"],
        user_id= dictCreateOrder["userId"],
        shop_id= dictCreateOrder["shopId"],
        deliveryAddressID = dictCreateOrder["deliveryAddressID"],
        products = list(map(mapCreateOrderProduct, dictCreateOrder["products"]))
    )

def mapCreateOrderProduct(dictProduct : dict) -> CreateOrderProduct:
    
    product = CreateOrderProduct(
        product_id= dictProduct["productId"],
        price= dictProduct["price"],
        quantity= dictProduct["quantity"],
        total= dictProduct["total"]
        )
    print(product)
    return product

def getOrderHistoryDelivering(request: HttpRequest) -> HttpResponse:
    return responseJson(get_delevering_order_history(userId=1))

def getOrderHistoryComplete(request: HttpRequest) -> HttpResponse:
    return responseJson(get_complete_order_history(userId=1)) 

@csrf_exempt
def rateOrder(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        try:
            with transaction.atomic():
                body: dict = json.loads(request.body)
                rateOrderRequest : RateOrderRequest = RateOrderRequest(
                    order_id= body["orderId"],
                    driver_score= body["driverScore"],
                    order_score= body["orderScore"]
                )
                return HttpResponse(status=rate_order(rateOrderRequest))
        except Exception as e:
            print(str(e))
            raise Http404("Does not exist") 
    else:
        raise Http404("Does not exist") 