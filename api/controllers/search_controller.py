from api.network_models import HotSearch, HotSearchKeyword, HotShop, ProductInGroup, ShopSearch, ShopProducts, ShopVoucher
from api.network_models import ProductGroup as ProductGroupNw
from django.db.models.query import QuerySet
from api.models import Merchant, MerchantVoucher, Product, ProductGroup, Voucher
from django.db.models import Q
import datetime
from typing import List

def get_hot_shop() -> HotSearch:
    dbModels: QuerySet[Merchant] = Merchant.objects.all().order_by('-rating_score_avg')[0:10]
    list_hot_shop : List[HotShop] = list(map(mapMerchant, dbModels))
    list_search_keyword : List[HotSearchKeyword] = list(map(mapKeyword,["Thịt","Cá","Trứng","Sữa"]))
    return HotSearch(shops=list_hot_shop, keywords=list_search_keyword)


def mapMerchant(merchant: Merchant) -> HotShop:
    return HotShop(id=merchant.id, name=merchant.name, thumb_url=merchant.thumbUrl.url, address=merchant.address, star=merchant.rating_score_avg)

def mapKeyword(name: str) -> HotSearchKeyword:
    return HotSearchKeyword(name=name)


def search_shop(keyword: str) -> List[ShopSearch]:
    dbModels: QuerySet[Merchant] = Merchant.objects.filter(Q(name__icontains = keyword)| Q(address__icontains = keyword) | Q(productgroup__name__icontains = keyword)).order_by('-rating_score_avg').distinct()
    list_shop_search : List[ShopSearch] = list(map(mapSearchMerchant, dbModels))
    return list_shop_search
 
def mapSearchMerchant(merchant: Merchant) -> ShopSearch:
    return ShopSearch(id=merchant.id, name=merchant.name, thumb_url=merchant.thumbUrl.url, address=merchant.address, star=merchant.rating_score_avg)

def shop_product(shopID : int) -> ShopProducts:
    try: 
        now: datetime = datetime.datetime.now()
        merchant : Merchant = Merchant.objects.get(id = shopID)
        dbProductGroup : QuerySet[ProductGroup] = merchant.productgroup_set.all()
        list_product_group : List[ProductGroupNw] = list(map(mapProductGroup, dbProductGroup))

        voucherModels: QuerySet[Voucher] = Voucher.objects.filter(last_date__gte=now, start_date__lte=now)
        voucherInWalletModels: QuerySet[Voucher] = MerchantVoucher.objects.filter(merchant__id=shopID).values('voucher_id')
        voucherInWalletIds: List[int] = list(map(lambda voucher: voucher["voucher_id"], voucherInWalletModels))
        dbModels: List[Voucher] = []
        for voucher in voucherModels:
            if voucher.id in voucherInWalletIds or voucher.isApplyAllBuyer == True:
                dbModels += [voucher]
        list_voucher : List[ShopVoucher] = list(map(mapMerchantVoucher, dbModels))

        return ShopProducts(shopId=merchant.id, shopName= merchant.name, shopAddress=merchant.address, groups=list_product_group, vouchers=list_voucher) 
    except Merchant.DoesNotExist:
        return None

def mapProductGroup(productGroup : ProductGroup) -> ProductGroupNw:
    productDb : QuerySet[Product] = Product.objects.filter(group_id = productGroup.id)
    list_products : List[Voucher] = list(map(mapProductInGroup, productDb))
    return ProductGroupNw(groupId=productGroup.id, groupName=productGroup.name, products = list_products)

def mapProductInGroup(product : Product) -> ProductInGroup:
    return ProductInGroup(productId = product.id, productName=product.name, productPrice=product.price, unit=product.unit_name, thumbUrl=product.thumbUrl.url)

def mapMerchantVoucher(voucher : Voucher):
    voucherdb : Voucher = Voucher.objects.get(id = voucher.id)
    return ShopVoucher(id=voucherdb.id, code=voucherdb.code, description=voucherdb.description)