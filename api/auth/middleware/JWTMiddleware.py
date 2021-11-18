from typing import Optional
from django.utils.deprecation import MiddlewareMixin
from django.http import HttpRequest
from api.auth.jwt_helper import decode_jwt_token
from api.auth.jwt_user import JWTUser, TokenExpiredError, HttpResponseAuthError

class JWTAuthenticationMiddleware(MiddlewareMixin):
    def process_request(self, request: HttpRequest):
        user: Optional[JWTUser] = None
        try:
            key_token = 'Authorization'
            
            if key_token in request.headers:
                jwt_token = request.headers[key_token]
                token_part = jwt_token.split(" ")
                user = decode_jwt_token(token_part[1])
        except TokenExpiredError:
            return HttpResponseAuthError()
        except:
            user = None

        setattr(request, 'jwt_user', user)