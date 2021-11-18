from django.urls import path

from api.api_views.home.banner import BannerApiView
from api.api_views.home.category import CategoryApiView
from api.api_views.order_history.history_complete import CompleteOrderHistoryApiView
from api.api_views.order_history.history_delevering import DeleveringOrderHistoryApiView
from api.api_views.order_history.order_detail import OrderDetailApiView
from api.api_views.voucher.voucher import VoucherApiView

from . import views

urlpatterns = [
    path('categories', CategoryApiView.as_view(), name='categories'),
    path('banners', BannerApiView.as_view(), name='banners'),
    path('voucher/list', VoucherApiView.as_view(), name='getListVoucher'),
    path('getHotSearch', views.getHotSearch, name='getHotSearch'),
    path('searchShop', views.searchShop, name='searchShop'),
    path('shop/<int:shopID>/products', views.products, name='productShop'),
    path('order/createOrder', views.createOrder, name= 'createOrder'),
    path("rateOrder", views.rateOrder, name="rateOrder"),
    path('order/<int:orderId>/deliveryInfo', views.deliveryInfo, name='deliveryInfo'),
    path('order/history/delivering', DeleveringOrderHistoryApiView.as_view(), name='getOrderHistoryDelivering'),
    path('order/history/complete', CompleteOrderHistoryApiView.as_view(), name='getOrderHistoryComplete'),
    path('order/<int:orderId>', OrderDetailApiView.as_view(), name='getOrderDetail'),
]

