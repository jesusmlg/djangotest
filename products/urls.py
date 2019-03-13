from django.contrib import admin
from django.urls import path
from products.views import product_detail_view, product_create_view, dynamic_lookup_view, product_delete_view, product_list_view

app_name = "products"

urlpatterns = [
  path('create/', product_create_view),
  path('<int:my_id>/', dynamic_lookup_view, name = 'detail_product'),
  path('<int:my_id>/delete', product_delete_view, name = 'delete_product'),
  path('', product_list_view, name = 'products')  
]