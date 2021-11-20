from django.views import View
from django.http import HttpRequest, HttpResponse
from api.auth.log_in_required_mixin import JwtLoginRequiredMixin
from api.controllers.order_history_controller import get_complete_order_history
from api.util import responseJson

class CompleteOrderHistoryApiView(JwtLoginRequiredMixin, View):
    def get(self, request: HttpRequest) -> HttpResponse:
        user_id = self.get_jwt_user_id(request)
        return responseJson(get_complete_order_history(user_id=user_id))


        