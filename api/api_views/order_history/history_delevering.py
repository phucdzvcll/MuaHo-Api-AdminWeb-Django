from django.views import View
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.order_history_controller import get_delevering_order_history
from django.http import HttpRequest, HttpResponse
from api.util import responseJson

class DeleveringOrderHistoryApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = self.get_jwt_user_id(request)
        return responseJson(get_delevering_order_history(userId=user_id))