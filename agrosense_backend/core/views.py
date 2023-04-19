from rest_framework import generics
from .models import Item, Inventory, StockTransactions, SupplierMaster, PurchaseOrderHeader, PurchaseOrderDetail, ProductionHeader, ProductionDetail, ProductionStatus, ItemPDetail, IndirectProductionExp, Immo
from .serializers import ItemSerializer, InventorySerializer, StockTransactionsSerializer, SupplierMasterSerializer, PurchaseOrderHeaderSerializer, PurchaseOrderDetailSerializer, ProductionHeaderSerializer, ProductionDetailSerializer, ProductionStatusSerializer, ItemPDetailSerializer, IndirectProductionExpSerializer, ImmoSerializer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class InventoryList(generics.ListCreateAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class InventoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer


class StockTransactionsList(generics.ListCreateAPIView):
    queryset = StockTransactions.objects.all()
    serializer_class = StockTransactionsSerializer


class StockTransactionsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockTransactions.objects.all()
    serializer_class = StockTransactionsSerializer


class SupplierMasterList(generics.ListCreateAPIView):
    queryset = SupplierMaster.objects.all()
    serializer_class = SupplierMasterSerializer


class SupplierMasterDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SupplierMaster.objects.all()
    serializer_class = SupplierMasterSerializer


class PurchaseOrderHeaderList(generics.ListCreateAPIView):
    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer


class PurchaseOrderHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderHeader.objects.all()
    serializer_class = PurchaseOrderHeaderSerializer


class PurchaseOrderDetailList(generics.ListCreateAPIView):
    queryset = PurchaseOrderDetail.objects.all()
    serializer_class = PurchaseOrderDetailSerializer


class PurchaseOrderDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrderDetail.objects.all()
    serializer_class = PurchaseOrderDetailSerializer


class ProductionHeaderList(generics.ListCreateAPIView):
    queryset = ProductionHeader.objects.all()
    serializer_class = ProductionHeaderSerializer


class ProductionHeaderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionHeader.objects.all()
    serializer_class = ProductionHeaderSerializer


class ProductionDetailList(generics.ListCreateAPIView):
    queryset = ProductionDetail.objects.all()
    serializer_class = ProductionDetailSerializer


class ProductionDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionDetail.objects.all()
    serializer_class = ProductionDetailSerializer


class ProductionStatusList(generics.ListCreateAPIView):
    queryset = ProductionStatus.objects.all()
    serializer_class = ProductionStatusSerializer


class ProductionStatusDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductionStatus.objects.all()
    serializer_class = ProductionStatusSerializer


class ItemPDetailList(generics.ListCreateAPIView):
    queryset = ItemPDetail.objects.all()
    serializer_class = ItemPDetailSerializer


class ItemPDetailDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ItemPDetail.objects.all()
    serializer_class = ItemPDetailSerializer


class IndirectProductionExpList(generics.ListCreateAPIView):
    queryset = IndirectProductionExp.objects.all()
    serializer_class = IndirectProductionExpSerializer


class IndirectProductionExpDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = IndirectProductionExp.objects.all()
    serializer_class = IndirectProductionExpSerializer


class ImmoList(generics.ListCreateAPIView):
    queryset = Immo.objects.all()
    serializer_class = ImmoSerializer


class ImmoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Immo.objects.all()
    serializer_class = ImmoSerializer
