# Django Libs:
from django.contrib import admin
# Local Libs:
from .models import AdBanner, Buyer, BuyerAddress, BuyerLoginInfo, BuyerVoucher, Driver, DriverOrderRating, Merchant, MerchantBuyerFavorite, MerchantCategory, MerchantVoucher, Order, OrderProduct, Product, ProductGroup, Voucher

admin.site.register(AdBanner)

admin.site.register(Buyer)

admin.site.register(BuyerAddress)

admin.site.register(BuyerLoginInfo,)


admin.site.register(BuyerVoucher)

admin.site.register(Driver)

admin.site.register(DriverOrderRating)

admin.site.register(Merchant)

admin.site.register(MerchantBuyerFavorite)

admin.site.register(MerchantCategory)

admin.site.register(MerchantVoucher)

admin.site.register(Order)

admin.site.register(OrderProduct)

admin.site.register(Product)

admin.site.register(ProductGroup)

admin.site.register(Voucher)
