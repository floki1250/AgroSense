from rest_framework.authtoken.views import obtain_auth_token
from rest_framework import routers
from django.contrib import admin
from django.urls import path, include
from core import views

router = routers.DefaultRouter()
urlpatterns = [
    path('items/', views.ItemList.as_view(), name='item-list'),
    path('items/<str:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('inventory/', views.InventoryList.as_view(), name='inventory-list'),
    path('inventory/<int:pk>/', views.InventoryDetail.as_view(),
         name='inventory-detail'),
    path('stocktransactions/', views.StockTransactionsList.as_view(),
         name='stocktransactions-list'),
    path('stocktransactions/<int:pk>/',
         views.StockTransactionsDetail.as_view(), name='stocktransactions-detail'),
    path('suppliermaster/', views.SupplierMasterList.as_view(),
         name='suppliermaster-list'),
    path('suppliermaster/<int:pk>/', views.SupplierMasterDetail.as_view(),
         name='suppliermaster-detail'),
    path('purchaseorderheader/', views.PurchaseOrderHeaderList.as_view(),
         name='purchaseorderheader-list'),
    path('purchaseorderheader/<int:pk>/',
         views.PurchaseOrderHeaderDetail.as_view(), name='purchaseorderheader-detail'),
    path('purchaseorderdetail/', views.PurchaseOrderDetailList.as_view(),
         name='purchaseorderdetail-list'),
    path('purchaseorderdetail/<int:pk>/',
         views.PurchaseOrderDetailDetail.as_view(), name='purchaseorderdetail-detail'),
]
