from calendar import c
import datetime
from this import d
from typing import List, Optional

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

    def __init__(self, id: int, name: str, address: str, thumb_url: str, star: float, location):  
        self.id = id
        self.name = name
        self.address = address
        self.thumb_url = thumb_url
        self.star = star
        self.location = location

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

    def __init__(self, product_id: int, price: float, quantity: int, total: float, product_name: str, product_thumb_url: str,):  
        self.productId = product_id
        self.price = price
        self.quantity = quantity
        self.total = total
        self.productName = product_name
        self.productThumbUrl = product_thumb_url

class OrderDetail():
    def __init__(self, order_id: int, products: List[OrderDetailProduct], voucher_code: str, total_before_discount: float, voucher_discount: float, total: float, delivery_address: str, delivery_phone_number: str, shop_id: int, shop_name: str, shop_address: str, status: str):  
        self.orderId = order_id
        self.products = products
        self.voucherCode = voucher_code
        self.totalBeforeDiscount = total_before_discount
        self.voucherDiscount = voucher_discount
        self.total = total
        self.deliveryAddress = delivery_address
        self.deliveryPhone_number = delivery_phone_number
        self.shopId = shop_id
        self.shopName = shop_name
        self.shopAddress = shop_address
        self.status = status

class OrderDeliveryInfo():

    def __init__(self, order_id: int, driver_name: str, driver_phone: str, plate_number: str, vehicle: str, total_order: float):  
        self.orderId = order_id
        self.driverName = driver_name
        self.driverPhone = driver_phone
        self.plateNumber = plate_number
        self.vehicle = vehicle
        self.totalOrder = total_order

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

    def __init__(self, status: str, orderId: Optional[int]):  
        self.status = status
        self.orderId = orderId


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

class CreateUserAddressRequest():
    def __init__(self, contact_phone_number: str, address: str, lat: float, lng: float):  
        self.contact_phone_number = contact_phone_number
        self.address = address
        self.lat = lat
        self.lng = lng

class UserAddressNetwork():
    def __init__(self, id: int, contact_phone_number: str, address: str, lat: float, lng: float, create_date):  
        self.id = id
        self.contact_phone_number = contact_phone_number
        self.address = address
        self.lat = lat
        self.lng = lng
        self.create_date = create_date

class Category():

    def __init__(self, id: int, name: str, thumb_url: str):  
        self.id = id
        self.name = name
        self.thumbUrl = thumb_url


class ShopSearchByCategory():

    def __init__(self, id: int, name: str, shopSearchs: List[ShopSearch]):
        self.id = id
        self.name = name
        self.shopSearchs = shopSearchs

class SignInNw():
    def __init__(self, jwt_token: str, user_name: str, refresh_token: str, email: str):  
        self.jwtToken = jwt_token
        self.userName = user_name
        self.email = email
        self.refreshToken = refresh_token

class RefreshTokenNw():
    def __init__(self, jwt_token: str):  
        self.jwtToken = jwt_token

class UserNameResponse():
    def __init__(self, user_name: str):  
        self.userName = user_name

class PhoneNumberResponse():
    def __init__(self, phone_number: str):  
        self.phoneNumber = phone_number

class MaintenanceResponse():
    def __init__(self, totalMinutes : int):
        self.totalMinutes = totalMinutes
        
class CheckMantenanceResponse():
    def __init__(self, maintenanceStatus : bool):
        self.maintenanceStatus = maintenanceStatus