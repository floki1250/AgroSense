from rest_framework import generics
from .models import Item, Inventory, StockTransactions, SupplierMaster, PurchaseOrderHeader, PurchaseOrderDetail
from .serializers import ItemSerializer, InventorySerializer, StockTransactionsSerializer, SupplierMasterSerializer, PurchaseOrderHeaderSerializer, PurchaseOrderDetailSerializer
from rest_framework.renderers import BrowsableAPIRenderer, JSONRenderer


class ItemList(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    renderer_classes = [BrowsableAPIRenderer, JSONRenderer]


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
