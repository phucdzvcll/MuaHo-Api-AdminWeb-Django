from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from api.models import Order, OrderProduct
from api.network_models import OrderDetail, OrderDetailProduct ,OrderHistory
from typing import List, Optional

def mapOrderStatus(orderStatus: str) -> str:
    for status in Order.STATUSES:
        if(orderStatus == status[0]):
            return status[1]
    return "unknown"

def mapOrderHistory(order: Order) -> OrderHistory:
    return OrderHistory(
        order_id=order.id,
        shop_name=order.merchant.name,
        item_count=order.item_count,
        total=order.total_amount,
        status=mapOrderStatus(order.order_status),
        order_code=order.code,
    )

def mapOrderStatus(orderStatus: str) -> str:
    for status in Order.STATUSES:
        if(orderStatus == status[0]):
            return status[1]

def mapOrderHistory(order: Order) -> OrderHistory:
    return OrderHistory(
        order_id=order.id,
        shop_name=order.merchant.name,
        item_count=order.item_count,
        total=order.total_amount,
        status=mapOrderStatus(order.order_status),
        order_code=order.code,
    )
def get_complete_order_history(userId: int) -> List[OrderHistory]:
    dbModels: QuerySet[Order] = Order.objects.filter(Q(buyer_id=userId) & (Q(order_status=Order.SUCCESS) | Q(order_status=Order.CANCEL) | Q(order_status=Order.FAIL))).select_related("merchant")
    list_history: List[OrderHistory] = list(map(mapOrderHistory, dbModels))
    return list_history


def get_delevering_order_history(userId: int) -> List[OrderHistory]:
    dbModels: QuerySet[Order] = Order.objects.filter(Q(buyer_id=userId) & (Q(order_status=Order.ACCEPTED) | Q(order_status=Order.DELIVERING) | Q(order_status=Order.PACKING))).select_related("merchant")
    list_history: List[OrderHistory] = list(map(mapOrderHistory, dbModels))
    return list_history
  
def mapOrderProductDetail(product: OrderProduct) -> OrderDetailProduct:
    return OrderDetailProduct(
        product_id=product.product.id,
        price=product.price,
        quantity=product.quantity,
        total=product.price * product.quantity, #miss total
    )

def mapOrderProduct(dbModels: QuerySet[OrderProduct]) -> List[OrderDetailProduct]:
    return list(map(mapOrderProductDetail, dbModels))

def get_order_detail(order_id: int) -> Optional[OrderDetail]:
    dbModel: Order = Order.objects.get(id=order_id)
    if dbModel != None:
        orderDetail : OrderDetail = OrderDetail(
            order_id=dbModel.id,
            products=mapOrderProduct(dbModel.orderproduct_set.all()),
            voucher_code=None if dbModel.voucher is None else dbModel.voucher.code, #miss voucher_code
            total_before_discount=0, #miss total_before_discount
            voucher_discount=0, #miss voucher_discount
            total=dbModel.total_amount,
            delivery_address=dbModel.delivery_address_text,
            delivery_phone_number=dbModel.delivery_phone_number,
            shop_id=dbModel.merchant.id,
            shop_name= dbModel.merchant.name, #miss shop_name
            shop_address=dbModel.merchant.address, #miss shop_address
            status=mapOrderStatus(dbModel.order_status),
        )
        return orderDetail
    return None
