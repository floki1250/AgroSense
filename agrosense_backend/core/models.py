from django.db import models
from django_extensions.db.models import TimeStampedModel

class Item(TimeStampedModel, models.Model):
    item_id = models.AutoField(primary_key=True)
    item_description = models.CharField(max_length=255,blank=True, null=True)
    unite_mesure = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)

    def __str__(self):
        return str(self.item_id)


class Inventory(TimeStampedModel, models.Model):
    item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
    quantity = models.IntegerField()
    unit_cost = models.FloatField()
    total_cost = models.FloatField()
    warehouse = models.CharField(max_length=255)
    item_type = models.CharField(max_length=255)
    item_measure = models.CharField(max_length=255)

    def __str__(self):
        return str(self.item_id)


class StockTransactions(TimeStampedModel, models.Model):
    transaction_id = models.AutoField(primary_key=True)
    item_id = models.IntegerField()
    transaction_type = models.CharField(max_length=255)
    quantity = models.IntegerField()
    cost = models.FloatField()
    transaction = models.DateTimeField()
    user_id = models.IntegerField()
    rmk = models.CharField(max_length=255,blank=True, null=True)


class SupplierMaster(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.CharField(max_length=255)
    supplier_contact = models.CharField(max_length=255)
    supplier_email = models.EmailField()


class PurchaseOrderHeader(models.Model):
    order_no = models.IntegerField(primary_key=True)
    order_type = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    supplier_id = models.IntegerField()
    requested_date = models.DateField(null=True)
    order_date = models.DateField()
    scheduled_pick_date = models.DateField(null=True)
    actual_ship_date = models.DateField(null=True)
    cancel_date = models.DateField(null=True)
    date_received = models.DateField(null=True)
    price_effective_date = models.DateField(null=True)
    promised_shipment_date = models.DateField(null=True)
    remark = models.TextField(blank=True, null=True)
    order_gross_amount = models.FloatField()
    currency_mode = models.CharField(max_length=255)
    foreign_open_amount = models.FloatField(null=True)
    status = models.CharField(max_length=255)


class PurchaseOrderDetail(models.Model):
    order_no = models.ForeignKey(PurchaseOrderHeader, on_delete=models.CASCADE)
    line_no = models.IntegerField()
    item_id = models.IntegerField()
    quantity = models.IntegerField()
    unit = models.CharField(max_length=255)
    unit_cost = models.FloatField()
    order_gross_amount = models.FloatField()
    currency_mode = models.CharField(max_length=255)
    foreign_amount = models.FloatField()
    status = models.CharField(max_length=255)


class ProductionHeader(models.Model):
    transaction_id = models.IntegerField(primary_key=True)
    lot_number = models.IntegerField()
    produced_item = models.CharField(max_length=255)
    estimated_amount = models.FloatField()
    start_date = models.DateField()
    estimated_end_date = models.DateField()
    surface = models.FloatField()
    current_status = models.CharField(max_length=255)
    final_status = models.CharField(max_length=255)


class ProductionDetail(models.Model):
    transaction_id = models.ForeignKey(ProductionHeader, on_delete=models.CASCADE)
    lineno = models.IntegerField()
    lot_number = models.IntegerField()
    item_id = models.IntegerField()
    estimated_quantity = models.IntegerField()
    real_quantity = models.IntegerField()
    estimated_amount = models.FloatField()
    real_amount = models.FloatField()
    start_date = models.DateField()
    end_date = models.DateField()


class ProductionStatus(models.Model):
    transaction_id = models.ForeignKey(ProductionHeader, on_delete=models.CASCADE)
    lineno = models.ForeignKey(ProductionDetail, on_delete=models.CASCADE)
    lot_number = models.IntegerField()
    status = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()


class ItemPDetail(models.Model):
    transaction_id = models.ForeignKey(ProductionHeader, on_delete=models.CASCADE)
    lineno = models.ForeignKey(ProductionDetail, on_delete=models.CASCADE)
    produced_item = models.CharField(max_length=255)
    composed_item = models.CharField(max_length=255)
    unite_mesure = models.CharField(max_length=255)

class IndirectProductionExp(models.Model):
    transaction_id = models.ForeignKey(ProductionHeader, on_delete=models.CASCADE)
    lineno = models.IntegerField(primary_key=True)
    lot_number = models.IntegerField()
    idimmo = models.CharField(max_length=255)
    description = models.TextField()
    unite_de_mesure = models.CharField(max_length=255)
    unit_cost = models.FloatField()
    quantity = models.IntegerField()
    amount = models.FloatField()


class Immo(models.Model):
    idimmo= models.AutoField(primary_key=True) 
    serial_number = models.TextField()
    description = models.TextField()
    date_of_commissioning = models.DateField()
    cost_account = models.FloatField()
    depreciation_period = models.IntegerField()
    amount_per_hour = models.FloatField(null=True)
    usage = models.FloatField()
    image = models.ImageField(upload_to='immo_images/',null=True)
    


class Land(models.Model):
    land_id = models.AutoField(primary_key=True)
    surface = models.JSONField()
    lat = models.FloatField()
    lang = models.FloatField()
    sensor_id = models.IntegerField()





