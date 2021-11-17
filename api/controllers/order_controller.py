from functools import cached_property
from api.network_models import CreateOrderRequest, CreateOrderRespone, OrderDeliveryInfo, RateOrderRequest
import datetime
from api.models import Buyer, BuyerAddress, Driver, Merchant, Order, OrderProduct, Product, Voucher

def create_order(createOrderRequest: CreateOrderRequest) -> CreateOrderRespone:
    now: datetime = datetime.datetime.now()

    item_count = 0
    for product in createOrderRequest.products:
        item_count += product.quantity
    
    merchant : Merchant = Merchant.objects.get(id = createOrderRequest.shopId)
    voucher : Voucher = None
    if createOrderRequest.voucherId is not None:
        voucher = Voucher.objects.get(id = createOrderRequest.voucherId)
    # check voucher discount
    # validator voucher (valid shope, valid user, expire time of voucher )
    # check total before discount and total amount
    buyer : Buyer = Buyer.objects.get(id = createOrderRequest.userId)
    buyer_address : BuyerAddress = BuyerAddress.objects.get(id = createOrderRequest.deliveryAddressID)

    order : Order = Order( 
        code = 'auto_gen', 
        merchant = merchant, 
        buyer = buyer, 
        delivery_address = buyer_address,
        delivery_address_text = buyer_address.address,
        delivery_phone_number = buyer_address.contact_phone_number,
        voucher = voucher,
        total_amount = createOrderRequest.total,
        voucher_discount = createOrderRequest.voucherDiscount,
        driver = None,
        order_status = Order.ACCEPTED,
        voucher_code = voucher.code if voucher is not None else None,
        total_before_discount = createOrderRequest.totalBeforeDiscount,
        shop_name = merchant.name,
        shop_address = merchant.address,
        item_count = item_count,
        order_date = now,
        last_update_date = now
    )
    order.save()

    # check price, check total price, check quantity > 0
    for requestPropduct in createOrderRequest.products:
        product : Product = Product.objects.get(id = requestPropduct.productId)
        order.orderproduct_set.create(
            product = product, 
            price = requestPropduct.price, 
            quantity = requestPropduct.quantity, 
            create_date = now, 
            product_name = product.name,
            total = requestPropduct.total
            )
    return CreateOrderRespone(status= 'success')



def get_order_delivery_info(order_id: int) -> OrderDeliveryInfo:
    return 'do some magic!'


def rate_order(rateOrderRequest: RateOrderRequest):
    pass
