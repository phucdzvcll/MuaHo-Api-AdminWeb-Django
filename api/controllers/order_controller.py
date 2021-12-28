from typing import Optional
from django.db.models import Avg
from django.db.models.query import QuerySet
from api.network_models import CreateOrderRequest, CreateOrderRespone, OrderDeliveryInfo, RateOrderRequest
import datetime
from api.models import Buyer, BuyerAddress, Driver, DriverOrderRating, Merchant, Order, OrderProduct, Product, Voucher
from django.db import transaction

def create_order(createOrderRequest: CreateOrderRequest) -> CreateOrderRespone:
    try:
        with transaction.atomic():
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
            return CreateOrderRespone(status= 'success', orderId= order.id)
    except Exception as e:
        return CreateOrderRespone(status= 'error', orderId= None)



def get_order_delivery_info(order_id: int) -> OrderDeliveryInfo:
    return 'do some magic!'


def rate_order(rateOrderResquest: RateOrderRequest, user_id: int) -> bool:
    order : Order
    try:
        with transaction.atomic():
            order = Order.objects.get(id = rateOrderResquest.orderId)
            
            if order.buyer.id != user_id:
                return False
            elif order.order_status != Order.SUCCESS and order.order_status != Order.FAIL:
                return False
            else:
                now: datetime = datetime.datetime.now()
                orderDriverRating : DriverOrderRating = DriverOrderRating(
                    order = order,
                    driver = order.driver,
                    driver_rating_score = rateOrderResquest.driverScore,
                    order_rating_score = rateOrderResquest.orderScore,
                    create_date = now
                )
                orderDriverRating.save()
                driver : Driver = Driver.objects.get(id = order.driver.id)
                driverScoreAvg : float = DriverOrderRating.objects.filter(driver__id = driver.id).aggregate(Avg('driver_rating_score'))["driver_rating_score__avg"]
                driver.rating_score_avg = driverScoreAvg
                driver.save(update_fields=['rating_score_avg'])

                merchant : Merchant = Merchant.objects.get(id = order.merchant.id)
                merchantScoreAvg : float = DriverOrderRating.objects.filter(driver__id = driver.id).aggregate(Avg('order_rating_score'))["order_rating_score__avg"]
                merchant.rating_score_avg = merchantScoreAvg
                merchant.save(update_fields=['rating_score_avg'])

                return True
    except Exception as e:
        return False

def order_delivery_infor(orderID : int, user_id: int) -> Optional[OrderDeliveryInfo]:
    try:
        order : Order = Order.objects.get(id = orderID)
        driver : Driver= order.driver
        if order.buyer.id != user_id:
            return None
        elif driver is None:
            return None
        else:
            return OrderDeliveryInfo(
                order_id= orderID, 
                driver_name= driver.name,
                driver_phone= driver.contact_phone_number,
                vehicle= driver.vehicle_info,
                plate_number= driver.vehicle_plate_number,
                total_order= order.total_amount)
    except Exception as e:
        return None