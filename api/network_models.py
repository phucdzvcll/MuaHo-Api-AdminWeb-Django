import datetime
from typing import List

class Banner():
    def __init__(self, id: int, subject: str, description: str, thumb_url: str, deeplink: str):
        self.id = id
        self.subject = subject
        self.description = description
        self.thumbUrl = thumb_url
        self.deeplink = deeplink

class Voucher():
    def __init__(self, id: int, code: str, description: str, value: float, type: str, min_order_total: float, is_apply_for_all_shop: bool, shops: List[int], last_date: datetime.datetime):  
        self.id = id
        self.code = code
        self.description = description
        self.value = value
        self.type = type
        self.min_order_total = min_order_total
        self.is_apply_for_all_shop = is_apply_for_all_shop
        self.shops = shops
        self.lastDate = last_date

class ShopVoucher():
    def __init__(self, id: int, code: str, description: str):
        self.id = id
        self.code = code
        self.description = description


class ShopSearch():

    def __init__(self, id: int, name: str, address: str, thumb_url: str, star: float):  
        self.id = id
        self.name = name
        self.address = address
        self.thumb_url = thumb_url
        self.star = star

class ProductInGroup():

    def __init__(self, productId: int, productName: str, productPrice: float, unit: str, thumbUrl: str):  
        self.productId = productId
        self.productName = productName
        self.produtPrice = productPrice
        self.unit = unit
        self.thumbUrl = thumbUrl

class ProductGroup():
    def __init__(self, groupId: int, groupName: str, products: List[ProductInGroup]):  
        self.groupId = groupId
        self.groupName = groupName
        self.products = products

class ShopProducts():

    def __init__(self, shopId: int, shopName: str, shopAddress: str, groups: List[ProductGroup], vouchers: List[ShopVoucher]):  
        self.shopId = shopId
        self.shopName = shopName
        self.shopAddress = shopAddress
        self.groups = groups
        self.vouchers = vouchers

class RateOrderRequest():

    def __init__(self, order_id: int, driver_score: int, order_score: int):  
        self.orderId = order_id
        self.driverScore = driver_score
        self.orderScore = order_score



class OrderHistory():

    def __init__(self, order_id: int, shop_name: str, order_code: str, item_count: int, total: float, status: str):  
        self.orderId = order_id
        self.orderCode = order_code
        self.shopName = shop_name
        self.itemCount = item_count
        self.total = total
        self.status = status

class OrderDetailProduct():

    def __init__(self, product_id: int, price: float, quantity: int, total: float):  
        self.product_id = product_id
        self.price = price
        self.quantity = quantity
        self.total = total

class OrderDetail():
    def __init__(self, order_id: int, products: List[OrderDetailProduct], voucher_code: str, total_before_discount: float, voucher_discount: float, total: float, delivery_address: str, delivery_phone_number: str, shop_id: int, shop_name: str, shop_address: str, status: str):  
        self.order_id = order_id
        self.products = products
        self.voucher_code = voucher_code
        self.total_before_discount = total_before_discount
        self.voucher_discount = voucher_discount
        self.total = total
        self.delivery_address = delivery_address
        self.delivery_phone_number = delivery_phone_number
        self.shop_id = shop_id
        self.shop_name = shop_name
        self.shop_address = shop_address
        self.status = status

class OrderDeliveryInfo():

    def __init__(self, order_id: int, driver_name: str, driver_phone: str, plate_number: str, vehicle: str, total_order: float):  
        self.order_id = order_id
        self.driver_name = driver_name
        self.driver_phone = driver_phone
        self.plate_number = plate_number
        self.vehicle = vehicle
        self.total_order = total_order

class HotShop():

    def __init__(self, id: int, name: str, address: str, thumb_url: str, star: float):  
        self.id = id
        self.name = name
        self.address = address
        self.thumbUrl = thumb_url
        self.star = star

class HotSearchKeyword():

    def __init__(self, name: str):  
        self.name = name

class HotSearch():

    def __init__(self, keywords: List[HotSearchKeyword], shops: List[HotShop]):  
        self.keywords = keywords
        self.shops = shops

class CreateOrderRespone():

    def __init__(self, status: str):  
        self.status = status


class CreateOrderProduct():

    def __init__(self, product_id: int, price: float, quantity: int, total: float):  
        self.productId = product_id
        self.price = price
        self.quantity = quantity
        self.total = total

    def __str__(self) -> str:
        return str(vars(self))

class CreateOrderRequest():

    def __init__(self, products: List[CreateOrderProduct], voucher_id: int, total_before_discount: float, voucher_discount: float, total: float, user_id: int, shop_id: int, deliveryAddressID: int):  
        self.products = products
        self.voucherId = voucher_id
        self.totalBeforeDiscount = total_before_discount
        self.voucherDiscount = voucher_discount
        self.total = total
        self.userId = user_id
        self.deliveryAddressID = deliveryAddressID
        self.shopId = shop_id



class Category():

    def __init__(self, id: int, name: str, thumb_url: str):  
        self.id = id
        self.name = name
        self.thumbUrl = thumb_url

