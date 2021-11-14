from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('banners', views.banners, name='banners'),
    path('voucher/list', views.getListVoucher, name='getListVoucher'),
    path('getHotSearch', views.getHotSearch, name='getHotSearch'),
    path('searchShop', views.searchShop, name='searchShop'),
    path('shop/<int:shopID>/products', views.products, name='productShop'),
    path('order/history/delivering', views.getOrderHistoryDelivering, name='getOrderHistoryDelivering'),
    path('order/history/complete', views.getOrderHistoryComplete, name='getOrderHistoryComplete'),
] 
