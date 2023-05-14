
from rest_framework import routers
from django.contrib import admin
from core import views
from django.urls import path, include


router = routers.DefaultRouter()
urlpatterns = [
    path("admin/", admin.site.urls),
    path('auth/', include('djoser.urls.jwt')),                                                    
    path('auth/', include('djoser.urls')),                                                        
    path('auth/', include('djoser.urls.authtoken')), 
    path("items/", views.ItemList.as_view(), name="item-list"),
    path("items/<str:pk>/", views.ItemDetail.as_view(), name="item-detail"),
    path("inventory/", views.InventoryList.as_view(), name="inventory-list"),
    path(
        "inventory/<int:pk>/", views.InventoryDetail.as_view(), name="inventory-detail"
    ),
    path(
        "stocktransactions/",
        views.StockTransactionsList.as_view(),
        name="stocktransactions-list",
    ),
    path(
        "stocktransactions/<int:pk>/",
        views.StockTransactionsDetail.as_view(),
        name="stocktransactions-detail",
    ),
    path(
        "suppliermaster/",
        views.SupplierMasterList.as_view(),
        name="suppliermaster-list",
    ),
    path(
        "suppliermaster/<int:pk>/",
        views.SupplierMasterDetail.as_view(),
        name="suppliermaster-detail",
    ),
    path(
        "purchaseorderheader/",
        views.PurchaseOrderHeaderList.as_view(),
        name="purchaseorderheader-list",
    ),
    path(
        "purchaseorderheader/<int:pk>/",
        views.PurchaseOrderHeaderDetail.as_view(),
        name="purchaseorderheader-detail",
    ),
    path(
        "purchaseorderdetail/",
        views.PurchaseOrderDetailList.as_view(),
        name="purchaseorderdetail-list",
    ),
    path(
        "purchaseorderdetail/<int:pk>/",
        views.PurchaseOrderDetailDetail.as_view(),
        name="purchaseorderdetail-detail",
    ),
    path(
        "productionheader/",
        views.ProductionHeaderList.as_view(),
        name="productionheader-list",
    ),
    path(
        "productionheader/<int:pk>/",
        views.ProductionHeaderDetail.as_view(),
        name="productionheader-detail",
    ),
    path(
        "productiondetail/",
        views.ProductionDetailList.as_view(),
        name="productiondetail-list",
    ),
    path(
        "productiondetail/<int:pk>/",
        views.ProductionDetailDetail.as_view(),
        name="productiondetail-detail",
    ),
    path(
        "productionstatus/",
        views.ProductionStatusList.as_view(),
        name="productionstatus-list",
    ),
    path(
        "productionstatus/<int:pk>/",
        views.ProductionStatusDetail.as_view(),
        name="productionstatus-detail",
    ),
    path("itempdetail/", views.ItemPDetailList.as_view(), name="itempdetail-list"),
    path(
        "itempdetail/<int:pk>/",
        views.ItemPDetailDetail.as_view(),
        name="itempdetail-detail",
    ),
    path(
        "indirectproductionexp/",
        views.IndirectProductionExpList.as_view(),
        name="indirectproductionexp-list",
    ),
    path(
        "indirectproductionexp/<int:pk>/",
        views.IndirectProductionExpDetail.as_view(),
        name="indirectproductionexp-detail",
    ),
    path("immo/", views.ImmoList.as_view(), name="immo-list"),
    path("immo/<int:pk>/", views.ImmoDetail.as_view(), name="immo-detail"),
    path(
        "recommend_water/",
        views.WaterRecommendationView.as_view(),
        name="recommend_water",
    ),
    path("land/", views.LandsList.as_view(), name="lands-list"),
    path("land/<int:pk>/", views.LandsDetail.as_view(), name="lands-detail"),
]
