from django.views import View
from django.http import HttpRequest, HttpResponse
from api.util import responseJson
from api.network_models import CreateOrderProduct, CreateOrderRequest
from django.views.decorators.csrf import csrf_exempt
from api.controllers.order_controller import create_order
import json
from django.utils.decorators import method_decorator
def mapCreateOrderProduct(dictProduct : dict) -> CreateOrderProduct:
        
        product = CreateOrderProduct(
            product_id= dictProduct["productId"],
            price= dictProduct["price"],
            quantity= dictProduct["quantity"],
            total= dictProduct["total"]
            )
        print(product)
        return product

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

@method_decorator(csrf_exempt, name='dispatch')
class CreateOrder(View):
    def post(self, request: HttpRequest) -> HttpResponse:
        body : dict = json.loads(request.body)
        createOrderRequestObj : CreateOrderProduct = mapCreateOrderRequest(body)
        return responseJson(create_order(createOrderRequestObj))