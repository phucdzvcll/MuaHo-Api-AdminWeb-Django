# Django Libs:
from django.contrib import admin
from django import forms
from django.db import models
from django.utils.html import format_html

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

class MerchantAdminForm(forms.ModelForm):
    class Meta:
        model = Merchant
        widgets = {
            'name': forms.TextInput(attrs={'size': "50"}),
            'address': forms.TextInput(attrs={'size': "80"}),
        }
        fields = '__all__'

class MerchantAdmin(admin.ModelAdmin):
    def thumbnail_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="64px" />'.format(obj.thumbUrl.url))
    thumbnail_preview.short_description = 'Thumbnail preview'

    def thumbnail_preview_detail(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.thumbUrl.url))
    thumbnail_preview_detail.short_description = 'Thumbnail preview'

    inlines = [ProductGroupInline]
    model = Merchant
    # Using for list category display
    list_display = ['id', 'name', 'rating_score_avg', 'thumbnail_preview']
    # # Using for detail display
    readonly_fields = ['thumbnail_preview_detail']
    list_display_links = ['id', 'rating_score_avg', "name", 'thumbnail_preview']
    form = MerchantAdminForm
    
admin.site.register(AdBanner)

admin.site.register(Buyer)

admin.site.register(BuyerAddress)

admin.site.register(BuyerLoginInfo,)


admin.site.register(BuyerVoucher)

admin.site.register(Driver)

admin.site.register(DriverOrderRating)

admin.site.register(Merchant, MerchantAdmin)

admin.site.register(MerchantBuyerFavorite)

class MerchantCategoryAdminForm(forms.ModelForm):
    class Meta:
        model = MerchantCategory
        widgets = {
            'name': forms.TextInput(attrs={'size': "50"})
        }
        fields = '__all__'

class MerchantCategoryAdmin(admin.ModelAdmin):
    # Thumbnail
    # https://sorl-thumbnail.readthedocs.io/en/latest/examples.html#admin-examples

    def thumbnail_preview(self, obj):
        return format_html('<img src="{}" width="auto" height="64px" />'.format(obj.thumbUrl.url))
    thumbnail_preview.short_description = 'Thumbnail preview'
    
    def thumbnail_preview_detail(self, obj):
        return format_html('<img src="{}" width="auto" height="200px" />'.format(obj.thumbUrl.url))
    thumbnail_preview_detail.short_description = 'Thumbnail preview'

    def edit_button(self, obj):
        return format_html('<a class="btn" href="/admin/api/merchantcategory/{}/change/"><input type="submit" value="Edit"></a>', obj.id)
    edit_button.short_description = 'Edit'

    def delete_button(self, obj):
        return format_html('<a class="btn" href="/admin/api/merchantcategory/{}/delete/"><input type="submit" value="Delete"></a>', obj.id)
    delete_button.short_description = 'Delete'
    
    model = MerchantCategory
    # Using for list category display
    list_display = ['id', 'name', 'thumbnail_preview', 'edit_button', 'delete_button']
    # Using for detail display
    readonly_fields = ['thumbnail_preview_detail']
    list_display_links = ['id', 'thumbnail_preview', "name"]
    form = MerchantCategoryAdminForm


admin.site.register(MerchantCategory, MerchantCategoryAdmin)

class OrderProductInline(admin.StackedInline):
    model = OrderProduct
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [OrderProductInline]

admin.site.register(Order, OrderAdmin)

admin.site.register(OrderProduct)

class ProductInlineForm(forms.ModelForm):
    class Meta:
        model = Product
        widgets = {
            'sku': forms.TextInput(attrs={'size': "50"}),
            'name': forms.TextInput(attrs={'size': "50"}),
            'unit_name': forms.TextInput(attrs={'size': "50"}),
        }
        fields = '__all__'

class ProductGroupAdminForm(forms.ModelForm):
    class Meta:
        model = ProductGroup
        widgets = {
            'name': forms.TextInput(attrs={'size': "50"})
        }
        fields = '__all__'

class ProductInlines(admin.StackedInline):
    model = Product
    extra = 1
    form = ProductInlineForm
    def thumbnail_preview_detail(self, obj):
        return format_html('<img src="{}" width="auto" height="100px" />'.format(obj.thumbUrl.url))
    thumbnail_preview_detail.short_description = 'Thumbnail preview'

    readonly_fields = ['thumbnail_preview_detail']

class ProductGroupAdmin(admin.ModelAdmin):
    form = ProductGroupAdminForm
    inlines = [ProductInlines]

admin.site.register(ProductGroup, ProductGroupAdmin)

class MerchantVoucherInline(admin.StackedInline):
    model = MerchantVoucher

class VoucherAdmin(admin.ModelAdmin):
    inlines = [MerchantVoucherInline]
    model = Voucher

admin.site.register(Voucher, VoucherAdmin)
