from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('categories', views.categories, name='categories'),
    path('getHotSearch', views.getHotSearch, name='getHotSearch'),
    path('searchShop', views.searchShop, name='searchShop'),
    path('shop/<int:shopID>/products', views.products, name='productShop')
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
