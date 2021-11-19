from typing import Optional
from api.network_models import SignInNw
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from firebase_admin import auth
from django.db import transaction
from api.auth.jwt_helper import encode_jwt_token
from api.auth.jwt_user import JWTUser, JWTUserRole
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
                buyer = Buyer(name= 'Guest')
                buyer.save()
                firebaseBuyer = FirebaseBuyer(uid = uid, buyer= buyer)
                firebaseBuyer.save()
        else:
            firebaseBuyer = FirebaseBuyer.objects.get(uid = uid)
            buyer = firebaseBuyer.buyer

        jwtUser = JWTUser(user_id= buyer.id, user_role= JWTUserRole.BUYER)
        jwtToken: str = encode_jwt_token(jwtUser, 30*60)
        result = SignInNw(jwt_token=jwtToken, user_name=buyer.name)
        return result
    except Exception as e:
        return None