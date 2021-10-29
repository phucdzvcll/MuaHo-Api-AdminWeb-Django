from api.network_models import CreateOrderRequest, CreateOrderRespone, OrderDeliveryInfo, RateOrderRequest

def create_order(createOrderRequest: CreateOrderRequest) -> CreateOrderRespone:
    return 'do some magic!'


def get_order_delivery_info(order_id: int) -> OrderDeliveryInfo:
    return 'do some magic!'


def rate_order(rateOrderRequest: RateOrderRequest):
    pass
