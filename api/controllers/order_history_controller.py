from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from api.models import Order
from api.network_models import OrderDetail ,OrderHistory
from typing import List
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


def get_order_detail(order_id: int) -> OrderDetail:
    
    return 'do some magic!'
