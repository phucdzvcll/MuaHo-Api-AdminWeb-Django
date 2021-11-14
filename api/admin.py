# Django Libs:
from django.contrib import admin
from django import forms
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
