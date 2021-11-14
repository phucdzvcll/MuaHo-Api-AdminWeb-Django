import datetime
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from api.network_models import Voucher as VoucherNetwork
from api.models import BuyerVoucher, Merchant, Voucher as VoucherDb
from typing import List

def mapMerchantCategory(voucherDb: VoucherDb) -> VoucherNetwork:
    voucherType : str = "percent"
    if voucherDb.voucher_type == VoucherDb.DISCOUNT:
        voucherType = "discount"
    #merchantVouchers = voucherDb.merchantvoucher_set.values('id')
    merchantVouchers = voucherDb.merchantvoucher_set.all()
    return VoucherNetwork(
        code= voucherDb.code,
        description= voucherDb.description,
        id= voucherDb.id,
        is_apply_for_all_shop= voucherDb.isApplyAllMerchant,
        shops= list(map(lambda merchant: merchant.id , merchantVouchers)),
        type= voucherType,
        value= voucherDb.value,
        min_order_total= voucherDb.min_order_total,
        last_date= voucherDb.last_date,
    )
    
def get_list_voucher(userId: int) -> List[VoucherNetwork]:
    now: datetime = datetime.datetime.now()
    voucherModels: QuerySet[VoucherDb] = VoucherDb.objects.filter(last_date__gte=now, start_date__lte=now).prefetch_related("merchantvoucher_set")
    voucherInWalletModels: QuerySet[VoucherDb] = BuyerVoucher.objects.filter(buyer__id=userId).values('voucher_id')

    voucherInWalletIds: List[int] = list(map(lambda voucher: voucher["voucher_id"], voucherInWalletModels))
    dbModels: List[VoucherDb] = []
    for voucher in voucherModels:
        if voucher.id in voucherInWalletIds or voucher.isApplyAllBuyer == True:
            dbModels += [voucher]
    
    list_voucher: List[VoucherNetwork] = list(map(mapMerchantCategory, dbModels))
    return list_voucher
