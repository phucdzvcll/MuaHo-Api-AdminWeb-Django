from django.http.request import HttpRequest
from api.auth.jwt_user import HttpResponseAuthError

class JwtLoginRequiredMixin:
    """Verify that the current user is authenticated."""
    def get_jwt_user_id(self, request: HttpRequest) -> int:
        return request.jwt_user.user_id

    def dispatch(self, request, *args, **kwargs):
        if not request.jwt_user:
            return HttpResponseAuthError()
        return super().dispatch(request, *args, **kwargs)