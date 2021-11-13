from api.network_models import HotSearch, HotSearchKeyword, HotShop, ShopSearch
from django.db.models.query import QuerySet
from api.models import Merchant, Product
from django.db.models import Q
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

# def shop_product(shopID : int) -> List[Product]:
    