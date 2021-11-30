from django.db.models.query import QuerySet
from api.models import AdBanner, MerchantCategory
from api.network_models import Banner, Category
from typing import List
import datetime

def mapBanner(adBanner: AdBanner) -> Banner:
    return Banner(
        id= adBanner.id, 
        subject= adBanner.subject, 
        description= adBanner.description, 
        thumb_url= adBanner.thumbUrl_url,
        deeplink= adBanner.deeplink_destination
    )

def mapThumbUrl(thumb_url):
    if thumb_url is not None:
        return thumb_url.url 
    else:
        return ""
def get_banners():
    now: datetime = datetime.datetime.now()
    dbModels: QuerySet[AdBanner] = AdBanner.objects.filter(end_date__gte=now, start_date__lte=now)
    list_banner: List[Banner] = list(map(mapBanner, dbModels))
    return list_banner

def mapMerchantCategory(merchantCategory: MerchantCategory) -> Category:
    return Category(id=merchantCategory.id, name=merchantCategory.name, thumb_url=merchantCategory.thumbUrl_url)

def get_categories() -> List[Category]:
    dbModels: QuerySet[MerchantCategory] = MerchantCategory.objects.all()
    list_category: List[Category] = list(map(mapMerchantCategory, dbModels))
    return list_category
