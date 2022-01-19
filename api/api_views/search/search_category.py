from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.network_models import ShopSearchByCategory
from api.util import responseJson
from django.http.response import HttpResponseNotFound
from api.controllers.search_controller import getMerchantByCategory


class SearchCategory(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest, categoryID: int) -> HttpResponse:

        merchant_result: ShopSearchByCategory = getMerchantByCategory(
            categoryID)

        if merchant_result is None:
            return HttpResponseNotFound()
        else:
            return responseJson(merchant_result)
