from api.controllers.home_controller import get_banners, get_categories
from django.http import HttpRequest, HttpResponse
from api.controllers.voucher_controller import get_list_voucher
from api.util import responseJson
from api.controllers import *
from django.http import Http404

def categories(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_categories())
    else:    
        raise Http404("Does not exist")

def banners(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_banners())
    else:    
        raise Http404("Does not exist")

def getListVoucher(request: HttpRequest) -> HttpResponse:
    if request.method == "GET":
        return responseJson(get_list_voucher(1))
    else:    
        raise Http404("Does not exist")
        