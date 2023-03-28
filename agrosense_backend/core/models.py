from django.db import models
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel
)


class Item(TimeStampedModel,
           ActivatorModel,
           TitleDescriptionModel,  models.Model):
    ItemID = models.CharField(max_length=255, primary_key=True)
    ItemDescription = models.CharField(max_length=255)
    UniteMesure = models.FloatField()
    ItemType = models.CharField(max_length=255)

    def __str__(self):
        return self.ItemID


class Inventory(TimeStampedModel, models.Model):
    ItemID = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    UnitCost = models.FloatField()
    TotalCost = models.FloatField()
    Warehouse = models.CharField(max_length=255)
    ItemType = models.CharField(max_length=255)
    ItemMeasure = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ItemID} ({self.Warehouse})'


class StockTransactions(TimeStampedModel, models.Model):
    TransactionID = models.AutoField(primary_key=True)
    ItemID = models.IntegerField()
    TransactionType = models.CharField(max_length=255)
    Quantity = models.IntegerField()
    Cost = models.FloatField()
    Transaction = models.DateTimeField()
    UserID = models.IntegerField()
    Rmk = models.CharField(max_length=255)


class SupplierMaster(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    supplier_name = models.CharField(max_length=255)
    supplier_address = models.CharField(max_length=255)
    supplier_contact = models.CharField(max_length=255)
    supplier_email = models.EmailField()


class PurchaseOrderHeader(models.Model):
    OrderNo = models.IntegerField(primary_key=True)
    OrderType = models.CharField(max_length=255)
    Company = models.IntegerField()
    supplier_id = models.IntegerField()
    RequestedDate = models.DateField()
    OrderDate = models.DateField()
    ScheduledPickDate = models.DateField()
    ActualShipDate = models.DateField()
    CancelDate = models.DateField()
    DateReceived = models.DateField()
    PriceEffectiveDate = models.DateField()
    PromisedShipmentDate = models.DateField()
    Remark = models.TextField()
    OrderGrossAmount = models.FloatField()
    CurrencyMode = models.CharField(max_length=255)
    ForeignOpenAmount = models.FloatField()
    status = models.CharField(max_length=255)


class PurchaseOrderDetail(models.Model):
    OrderNo = models.ForeignKey(PurchaseOrderHeader, on_delete=models.CASCADE)
    OrderType = models.CharField(max_length=255)
    Company = models.IntegerField()
    LineNo = models.IntegerField()
    ItemID = models.IntegerField()
    supplier_id = models.IntegerField()
    RequestedDate = models.DateField()
    DateReceived = models.DateField()
    OrderDate = models.DateField()
    ScheduledPickDate = models.DateField()
    ActualShipDate = models.DateField()
    CancelDate = models.DateField()
    PromisedShipmentDate = models.DateField()
    Remark = models.TextField()
    Quantity = models.IntegerField()
    Unit = models.CharField(max_length=255)
    UnitCost = models.FloatField()
    OrderGrossAmount = models.FloatField()
    CurrencyMode = models.CharField(max_length=255)
    ForeignAmount = models.FloatField()
    status = models.CharField(max_length=255)
