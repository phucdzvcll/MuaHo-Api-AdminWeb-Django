import datetime
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from api.network_models import CreateUserAddressRequest, UserAddressNetwork, Voucher as VoucherNetwork
from api.models import Buyer, BuyerAddress, BuyerVoucher, Merchant, Voucher as VoucherDb
from typing import List

def mapUserAddress(address: BuyerAddress) -> UserAddressNetwork:
    locations = address.location.split(",")

    if len(locations) != 2:
        locations = [0, 0]

    return UserAddressNetwork(
        address= address.address,
        id=address.id,
        contact_phone_number=address.contact_phone_number,
        lat=float(locations[0]),
        lng=float(locations[1]),
        create_date = address.create_date
    )
    
def get_list_address(user_id: int) -> List[UserAddressNetwork]:
    addressModels: QuerySet[BuyerAddress] = BuyerAddress.objects.filter(buyer__id=user_id)
    
    list_address: List[UserAddressNetwork] = list(map(mapUserAddress, addressModels))
    return list_address

def create_user_address(user_id: int, address: CreateUserAddressRequest) -> bool:
    try:
        now: datetime = datetime.datetime.now()
        location = "{lat},{lng}".format(lat = address.lat, lng = address.lng)
        buyer : Buyer = Buyer.objects.get(id = user_id)
        buyerAddress : BuyerAddress = BuyerAddress(
                        buyer = buyer,
                        address = address.address,
                        location = location,
                        contact_phone_number = address.contact_phone_number,
                        create_date= now,
                    )
        buyerAddress.save()
        return True
    except Exception as e:
        print("create_user_address", e)
        return False
    
