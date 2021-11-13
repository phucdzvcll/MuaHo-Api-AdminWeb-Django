# Django Libs:
from django.contrib import admin
from django import forms

# Local Libs:
from .models import AdBanner, Buyer, BuyerAddress, BuyerLoginInfo, BuyerVoucher, Driver, DriverOrderRating, Merchant, MerchantBuyerFavorite, MerchantCategory, MerchantVoucher, Order, OrderProduct, Product, ProductGroup, Voucher


class ProductGroupInlineAdminForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        widgets = {
            'name': forms.TextInput(attrs={'size': "50"})
        }
        fields = '__all__'

class ProductGroupInline(admin.StackedInline):
    model = ProductGroup
    form = ProductGroupInlineAdminForm

class MerchantAdmin(admin.ModelAdmin):
    inlines = [ProductGroupInline]
    model = Merchant

admin.site.register(AdBanner)

admin.site.register(Buyer)

admin.site.register(BuyerAddress)

admin.site.register(BuyerLoginInfo,)


admin.site.register(BuyerVoucher)

admin.site.register(Driver)

admin.site.register(DriverOrderRating)

admin.site.register(Merchant, MerchantAdmin)

admin.site.register(MerchantBuyerFavorite)

admin.site.register(MerchantCategory)

admin.site.register(Order)

admin.site.register(OrderProduct)

admin.site.register(Product)

class ProductGroupAdminForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        widgets = {
            'name': forms.TextInput(attrs={'size': "50"})
        }
        fields = '__all__'
    
class ProductGroupAdmin(admin.ModelAdmin):
    form = ProductGroupAdminForm

admin.site.register(ProductGroup, ProductGroupAdmin)

class MerchantVoucherInline(admin.StackedInline):
    model = MerchantVoucher

class VoucherAdmin(admin.ModelAdmin):
    inlines = [MerchantVoucherInline]
    model = Voucher

admin.site.register(Voucher, VoucherAdmin)
