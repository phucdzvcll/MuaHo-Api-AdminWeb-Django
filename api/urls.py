from django.urls import path

from . import views

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('banners', views.banners, name='banners'),
    path('voucher/list', views.getListVoucher, name='getListVoucher'),
] 
