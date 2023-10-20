from django.urls import path
from . import views


urlpatterns = [
    path('', views.products, name='products'),
    path('clients/', views.clients, name='clients'),
    path('orders/', views.orders, name='orders'),
    path('product/<int:id_pr>', views.product, name='product'),
    path('csp/<int:id_client>/<int:days>/', views.clients_sorted_products, name='clients_sorted_products'),
    path('client_orders/<int:id_client>', views.client_orders, name='client_orders'),
    path('product_form/<int:id_pr>', views.product_form, name='product_form'),
    path('edit_product_by_id/', views.edit_product_by_id, name='edit_product_by_id'),
    path('get_product/', views.edit_product, name='get_product'),

]

