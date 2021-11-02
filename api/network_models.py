from typing import List

class Banner():
    def __init__(self, id: int, subject: str, description: str, thumb_url: str):
        self._id = id
        self._subject = subject
        self._description = description
        self._thumb_url = thumb_url

class Voucher():
    def __init__(self, id: int, code: str, description: str, value: float, type: str, min_order_total: float, is_apply_for_all_shop: bool, shops: List[int]):  
        self._id = id
        self._code = code
        self._description = description
        self._value = value
        self._type = type
        self._min_order_total = min_order_total
        self._is_apply_for_all_shop = is_apply_for_all_shop
        self._shops = shops

class ShopVoucher():
    def __init__(self, id: int, code: str, description: str):
        self._id = id
        self._code = code
        self._description = description


class ShopSearch():

    def __init__(self, id: int, name: str, address: str, thumb_url: str, star: float):  
        self._id = id
        self._name = name
        self._address = address
        self._thumb_url = thumb_url
        self._star = star

class ProductInGroup():

    def __init__(self, product_id: int, product_name: str, produt_price: float, unit: str, thumb_url: str):  
        self._product_id = product_id
        self._product_name = product_name
        self._produt_price = produt_price
        self._unit = unit
        self._thumb_url = thumb_url

class ProductGroup():
    def __init__(self, group_id: int, group_name: str, products: List[ProductInGroup]):  
        self._group_id = group_id
        self._group_name = group_name
        self._products = products

class ShopProducts():

    def __init__(self, shop_id: int, shop_name: str, shop_address: str, groups: List[ProductGroup], vouchers: List[ShopVoucher]):  
        self._shop_id = shop_id
        self._shop_name = shop_name
        self._shop_address = shop_address
        self._groups = groups
        self._vouchers = vouchers

class RateOrderRequest():

    def __init__(self, order_id: int, driver_score: int, order_score: int):  
        self._order_id = order_id
        self._driver_score = driver_score
        self._order_score = order_score



class OrderHistory():

    def __init__(self, order_id: int, shop_name: str, item_count: int, total: float, status: str):  
        self._order_id = order_id
        self._shop_name = shop_name
        self._item_count = item_count
        self._total = total
        self._status = status

class OrderDetailProduct():

    def __init__(self, product_id: int, price: float, quantity: int, total: float):  
        self._product_id = product_id
        self._price = price
        self._quantity = quantity
        self._total = total

class OrderDetail():
    def __init__(self, order_id: int, products: List[OrderDetailProduct], voucher_code: str, total_before_discount: float, voucher_discount: float, total: float, delivery_address: str, delivery_phone_number: str, shop_id: int, shop_name: str, shop_address: str, status: str):  
        self._order_id = order_id
        self._products = products
        self._voucher_code = voucher_code
        self._total_before_discount = total_before_discount
        self._voucher_discount = voucher_discount
        self._total = total
        self._delivery_address = delivery_address
        self._delivery_phone_number = delivery_phone_number
        self._shop_id = shop_id
        self._shop_name = shop_name
        self._shop_address = shop_address
        self._status = status

class OrderDeliveryInfo():

    def __init__(self, order_id: int, driver_name: str, driver_phone: str, plate_number: str, vehicle: str, total_order: float):  
        self._order_id = order_id
        self._driver_name = driver_name
        self._driver_phone = driver_phone
        self._plate_number = plate_number
        self._vehicle = vehicle
        self._total_order = total_order

class HotShop():

    def __init__(self, id: int, name: str, address: str, thumb_url: str):  
        self._id = id
        self._name = name
        self._address = address
        self._thumb_url = thumb_url

class HotSearchKeyword():

    def __init__(self, name: str):  
        self._name = name

class HotSearch():

    def __init__(self, keywords: List[HotSearchKeyword], shops: List[HotShop]):  
        self._keywords = keywords
        self._shops = shops

class CreateOrderRespone():

    def __init__(self, status: str):  
        self._status = status


class CreateOrderProduct():

    def __init__(self, product_id: int, price: float, quantity: int, total: float):  
        self._product_id = product_id
        self._price = price
        self._quantity = quantity
        self._total = total

class CreateOrderRequest():

    def __init__(self, products: List[CreateOrderProduct], voucher_id: int, total_before_discount: float, voucher_discount: float, total: float, user_id: int, delivery_address: str, delivery_phone_number: str, shop_id: int):  
        self._products = products
        self._voucher_id = voucher_id
        self._total_before_discount = total_before_discount
        self._voucher_discount = voucher_discount
        self._total = total
        self._user_id = user_id
        self._delivery_address = delivery_address
        self._delivery_phone_number = delivery_phone_number
        self._shop_id = shop_id



class Category():

    def __init__(self, id: int, name: str, thumb_url: str):  
        self._id = id
        self._name = name
        self._thumb_url = thumb_url

