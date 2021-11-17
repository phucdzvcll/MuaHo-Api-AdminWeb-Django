from django.views import View
from api.controllers.voucher_controller import get_list_voucher
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class VoucherApiView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return responseJson(get_list_voucher(1))