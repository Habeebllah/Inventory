from .views import *
from django.urls import path, include
from knox import views as knox_views

from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from knox.views import LogoutView

from .views import *




schema_view = get_schema_view(
   openapi.Info(
      title="Couone MyStore API",
      default_version='v1',
      description="Couone MyStore App",
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [


    path('user', UserAPIView.as_view()),
    path('customerregister/', CustomerRegisterAPIView.as_view()),
    path('salesregister/', SalesRegisterAPIView.as_view()),
    path('login/', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),
   path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),

    path('doc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('category/', CategoryListCreateAPIView.as_view(), name='category-view'),
    path('supplier/', SupplierListAPIView.as_view(), name='supplier-view'),

    path('supplierdetails/<pk>/', SupplierDetailsAPIView.as_view(), name='supplierdetails-view'),
    path('categorydetails/<pk>/', CategoryDetailsAPIView.as_view(), name='categorydetails-view'),
    
    path('addinventory/', InventoryCreateAPIView.as_view(), name='addinventory'),
    path('inventory/', InventoryListAPIView.as_view(), name='inventory-view'),
    
    path('inventorydetails/<pk>/', InventoryDetailsAPIView.as_view(), name='inventorydetails-view'),


    path('order/', OrderCreateAPIView.as_view(), name='order-create'),

    path('orderlist/', OrderListAPIView.as_view(), name='orderlist-create'),
    

    

    path('sellerorder/<int:user_id>/', SellerOrderListCreateAPIView.as_view(), name='sellerorder-view'),


    path('addorderitem/', OrderItemCreateAPIView.as_view(), name='ordeiitem-create'),

    path('orderitemdetails/<pk>', OrderItemDetailsAPIView.as_view(), name='ordeiitem-view'),

    path('selleraddorderitemdetails/<pk>', SellerOrderItemListAPIView.as_view(), name='sellerordeiitem-view'),


    path('sellerdetailsdeleteorderitem/<pk>', SellerOrderItemRetreiveDeleteAPIView.as_view(), name='sellerordeitem-details'),




    





    




    

     


    

    

] 