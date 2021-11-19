import enum
from django.http import HttpResponse
from django.http.request import HttpRequest

class HttpResponseAuthError(HttpResponse):
    status_code = 401

class TokenExpiredError(Exception):
    pass

class JWTUserRole(enum.Enum):
    BUYER = "buyer"
    MERCHANT_OWNER = "merchaner_owner"

class JWTUser:
    def __init__(self, user_id: int, user_role: JWTUserRole) -> None:
        self.user_id = user_id
        self.user_role = user_role

def get_jwt_user_id(request: HttpRequest) -> int:
    return request.jwt_user.user_id
