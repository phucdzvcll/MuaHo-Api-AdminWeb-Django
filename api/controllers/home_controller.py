from django.db.models.query import QuerySet
from api.models import MerchantCategory
from api.network_models import Banner, Category
from typing import List

def get_banners():
    list_banner: List[Banner] = []

    return list_banner

def mapMerchantCategory(merchantCategory: MerchantCategory) -> Category:
    return Category(id=merchantCategory.id, name=merchantCategory.name, thumb_url=merchantCategory.thumbUrl)

def get_categories() -> List[Category]:
    dbModels: QuerySet[MerchantCategory] = MerchantCategory.objects.all()
    list_category: List[Category] = list(map(mapMerchantCategory, dbModels))
    return list_category
