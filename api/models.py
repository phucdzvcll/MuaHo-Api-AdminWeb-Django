from django.db import models

class AdBanner(models.Model):
    id = models.AutoField(primary_key=True)
    subject = models.TextField()
    description = models.TextField()
    deeplink_destination = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    thumbUrl = models.ImageField(upload_to='banner')

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = 'AdBanner'


class Buyer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    phone_number = models.TextField()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'Buyer'


class BuyerAddress(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_column='buyerId', db_constraint=False)
    address = models.TextField()
    contact_phone_number = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.address}"

    class Meta:
        managed = True
        db_table = 'BuyerAddress'


class BuyerLoginInfo(models.Model):
    buyer = models.OneToOneField(
        Buyer,
        on_delete=models.DO_NOTHING,
        primary_key=True,
        db_constraint=False
    )
    user_name = models.TextField(unique=True)
    user_3rd_id = models.TextField(blank=True, null=True)
    token = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.id} - {self.user_name}"

    class Meta:
        managed = True
        db_table = 'BuyerLoginInfo'


class BuyerVoucher(models.Model):
    id = models.AutoField(primary_key=True)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, db_constraint=False)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = 'BuyerVoucher'


class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    vehicle_info = models.TextField()
    vehicle_plate_number = models.TextField()
    contact_phone_number = models.TextField()
    rating_score_avg = models.FloatField()
    create_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'Driver'


class DriverOrderRating(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey('Order', models.DO_NOTHING, db_constraint=False)
    driver = models.ForeignKey(Driver, models.DO_NOTHING, db_constraint=False)
    driver_rating_score = models.FloatField()
    order_rating_score = models.FloatField()
    create_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = 'DriverOrderRating'


class Merchant(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    location_lat = models.FloatField()
    location_lng = models.FloatField()
    category = models.ForeignKey('MerchantCategory', models.DO_NOTHING, db_constraint=False)
    rating_score_avg = models.FloatField()

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'Merchant'


class MerchantBuyerFavorite(models.Model):
    id = models.AutoField(primary_key=True)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_constraint=False)
    merchant = models.ForeignKey(Merchant, models.DO_NOTHING, db_constraint=False)
    date = models.DateTimeField()
    status = models.BooleanField()

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = 'MerchantBuyerFavorite'


class MerchantCategory(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField()
    thumbUrl = models.ImageField(upload_to='category')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'MerchantCategory'


class MerchantVoucher(models.Model):
    id = models.AutoField(primary_key=True)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, db_constraint=False)
    merchant = models.ForeignKey(Merchant, models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f"{self.id}"

    class Meta:
        managed = True
        db_table = 'MerchantVoucher'


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.TextField(blank=True, null=True)
    merchantid = models.ForeignKey(Merchant, models.DO_NOTHING, db_column='merchantId', db_constraint=False)
    buyer = models.ForeignKey(Buyer, models.DO_NOTHING, db_column='buyerId', db_constraint=False)
    delivery_address = models.ForeignKey(BuyerAddress, models.DO_NOTHING, db_constraint=False)
    delivery_address_text = models.TextField(db_column='delivery_address', blank=True, null=True)
    delivery_phone_number = models.TextField(blank=True, null=True)
    voucher = models.ForeignKey('Voucher', models.DO_NOTHING, blank=True, null=True, db_constraint=False)
    total_amount = models.FloatField()
    driver = models.ForeignKey(Driver, models.DO_NOTHING, blank=True, null=True, db_constraint=False)
    status = models.IntegerField()
    order_date = models.DateTimeField()
    last_update_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - {self.code}"

    class Meta:
        managed = True
        db_table = 'Order'


class OrderProduct(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, models.DO_NOTHING, db_constraint=False)
    product = models.ForeignKey('Product', models.DO_NOTHING, db_constraint=False)
    price = models.FloatField()
    quantity = models.IntegerField()
    create_date = models.DateTimeField()

    def __str__(self):
        return f"{self.id} - Product: {self.product}"

    class Meta:
        managed = True
        db_table = 'OrderProduct'


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    sku = models.TextField(unique=True)
    name = models.TextField()
    price = models.FloatField()
    unit_name = models.TextField(blank=True)
    group = models.ForeignKey('ProductGroup', models.DO_NOTHING, db_constraint=False)
    merchant = models.ForeignKey(Merchant, models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'Product'


class ProductGroup(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    merchant = models.ForeignKey(Merchant, models.DO_NOTHING, db_constraint=False)

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'ProductGroup'


class Voucher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.TextField(blank=True, null=True)
    type = models.IntegerField(blank=True, null=True)
    value = models.FloatField()
    isApplyAllMerchant = models.BooleanField(db_column='isApplyAllMerchant')
    isApplyAllBuyer = models.BooleanField(db_column='isApplyAllBuyer')

    def __str__(self):
        return f"{self.id} - {self.name}"

    class Meta:
        managed = True
        db_table = 'Voucher'
