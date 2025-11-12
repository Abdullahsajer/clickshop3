from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('cart/', views.cart_view, name='cart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('checkout/', views.checkout_view, name='checkout'),
    path('orders/', views.my_orders_view, name='my_orders'),
    path('orders/<int:order_id>/', views.order_detail_view, name='order_detail'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('update/<int:item_id>/', views.update_cart_item, name='update_cart_item'),


]
