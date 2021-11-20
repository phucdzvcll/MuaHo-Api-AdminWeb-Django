from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.voucher_controller import get_list_voucher
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class VoucherApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = self.get_jwt_user_id(request)
        return responseJson(get_list_voucher(user_id=user_id))