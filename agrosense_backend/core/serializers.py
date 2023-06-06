from rest_framework import serializers
from .models import (
    Item,
    Inventory,
    StockTransactions,
    SupplierMaster,
    PurchaseOrderHeader,
    PurchaseOrderDetail,
    ProductionHeader,
    ProductionDetail,
    ProductionStatus,
    ItemPDetail,
    IndirectProductionExp,
    Immo,
    Land
)


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = "__all__"


class StockTransactionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = StockTransactions
        fields = "__all__"


class SupplierMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupplierMaster
        fields = "__all__"


class PurchaseOrderHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderHeader
        fields = "__all__"


class PurchaseOrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseOrderDetail
        fields = "__all__"


class ProductionHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionHeader
        fields = "__all__"


class ProductionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionDetail
        fields = "__all__"


class ProductionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductionStatus
        fields = "__all__"


class ItemPDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemPDetail
        fields = "__all__"


class IndirectProductionExpSerializer(serializers.ModelSerializer):
    class Meta:
        model = IndirectProductionExp
        fields = "__all__"


class ImmoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Immo
        fields = "__all__"


class LandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Land
        fields = "__all__"


class WaterRecommendationSerializer(serializers.Serializer):
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    category = serializers.IntegerField()


