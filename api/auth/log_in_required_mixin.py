from api.auth.jwt_user import HttpResponseAuthError

class JwtLoginRequiredMixin:
    """Verify that the current user is authenticated."""
    def dispatch(self, request, *args, **kwargs):
        if not request.jwt_user:
            return HttpResponseAuthError()
        return super().dispatch(request, *args, **kwargs)