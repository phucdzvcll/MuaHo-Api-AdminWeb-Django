import json
from typing import Optional
from api.network_models import PhoneNumberResponse, RefreshTokenNw, SignInNw, UserNameResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firebase_admin import auth
from django.db import transaction
from api.auth.jwt_helper import decode_jwt_token, encode_jwt_token
from api.auth.jwt_user import HttpResponseAuthError, JWTUser, JWTUserRole, TokenExpiredError
from api.models import Buyer, FirebaseBuyer

def sign_in(firebaseToken: str) -> Optional[SignInNw]: 
    try:
        decoded_token = auth.verify_id_token(firebaseToken)
        uid = decoded_token['uid']
        isUserExists = FirebaseBuyer.objects.filter(uid = uid).exists()
        buyer : Buyer
        firebaseBuyer : FirebaseBuyer
        if not isUserExists:
            with transaction.atomic():
                buyer = Buyer(name= "Guest", email = "")
                buyer.save()
                firebaseBuyer = FirebaseBuyer(uid = uid, buyer= buyer)
                firebaseBuyer.save()
        else:
            user: auth.UserRecord = auth.get_user(uid)
            email = user.email
            displayName = user.display_name
            firebaseBuyer = FirebaseBuyer.objects.get(uid = uid)
            buyer = firebaseBuyer.buyer
            buyer.name = displayName
            buyer.email = email
            buyer.save()
        jwtUser = JWTUser(user_id= buyer.id, user_role= JWTUserRole.BUYER)
        jwtToken: str = encode_jwt_token(jwtUser, 30*60)
        jwtRefreshToken: str = encode_jwt_token(jwtUser, 60*60*24*30)
        result = SignInNw(jwt_token=jwtToken, user_name=buyer.name, refresh_token= jwtRefreshToken, email= buyer.email)
        return result
    except Exception as e:
        return None

def update_user_name(user_name: str, userId: int) -> Optional[UserNameResponse]:
    try:
        buyer : Buyer = Buyer.objects.get(id = userId)
        buyer.name = user_name
        buyer.save()
        return UserNameResponse(user_name = buyer.name)
    except Exception as e:
        return None

def update_contact_phone(phoneNumber: str, userId: int) -> Optional[PhoneNumberResponse]:
    try:
        buyer : Buyer = Buyer.objects.get(id = userId)
        buyer.phone_number = phoneNumber
        buyer.save()
        return PhoneNumberResponse(phone_number= buyer.phone_number)
    except Exception as e:
        return None

class RefreshTokenResult:
     def __init__(self, token: Optional[RefreshTokenNw], isExpire: bool):  
        self.token = token
        self.isExpire = isExpire

def refresh_token(jwt_token: str) -> RefreshTokenResult:
    try:
        user = decode_jwt_token(jwt_token)
        jwtToken : str = encode_jwt_token(user= user, expSecondsFromNow= 30*60)
        result : RefreshTokenNw = RefreshTokenNw(jwt_token= jwtToken)
        return RefreshTokenResult(token= result, isExpire= False)
    except TokenExpiredError:
        return RefreshTokenResult(token= None, isExpire= True)
    except:
        return RefreshTokenResult(token= None, isExpire= False)
