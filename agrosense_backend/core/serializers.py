from rest_framework import serializers
from .models import Item, Inventory, StockTransactions, SupplierMaster, PurchaseOrderHeader, PurchaseOrderDetail

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = '__all__'


class StockTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransactions
        fields = '__all__'


class SupplierMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierMaster
        fields = '__all__'


class PurchaseOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderHeader
        fields = '__all__'


class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderDetail
        fields = '__all__'
