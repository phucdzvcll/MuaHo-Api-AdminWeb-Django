from typing import Optional
import jwt
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
import datetime

from api.auth.jwt_user import JWTUser, JWTUserRole, TokenExpiredError

def encode_jwt_token(user: JWTUser, expSecondsFromNow: int) -> str:
    key = getattr(settings, 'JWT_HS256_KEY', None)
    if not key:
        raise ImproperlyConfigured('Missing setting JWT_HS256_KEY')
    payload = {
        "user_id": user.user_id, 
        "role": user.user_role.value, 
        'exp': datetime.datetime.utcnow() + datetime.timedelta(seconds=expSecondsFromNow),
    }

    encoded: str = jwt.encode(payload, key, algorithm="HS256")
    return encoded

def mapUserRole(roleValue: str) -> JWTUserRole:
    if roleValue == JWTUserRole.MERCHANT_OWNER.value:
        return JWTUserRole.MERCHANT_OWNER
    else:
        return JWTUserRole.BUYER

def decode_jwt_token(jwt_token: Optional[str]) -> Optional[JWTUser]:
    key = getattr(settings, 'JWT_HS256_KEY', None)
    if not key:
        raise ImproperlyConfigured('Missing setting JWT_HS256_KEY')
    if not jwt_token:
        return None
    now = datetime.datetime.utcnow()
    try:
        payload = jwt.decode(jwt_token, key, algorithms="HS256")
        return JWTUser(
            user_id= payload["user_id"],
            user_role= mapUserRole(payload["role"]),
        )
    except jwt.ExpiredSignatureError:
        raise TokenExpiredError()
    except:
        return None