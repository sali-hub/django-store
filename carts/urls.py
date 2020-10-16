from django.urls import path
from .views import add_to_cart, cart, romove_from_cart
urlpatterns = [
path('carts/', cart,name='cart'),
path('carts/add/<int:product_id>/', add_to_cart,name='add_to_cart'),
path('carts/romove_from_cart/<int:product_id>/', romove_from_cart,name='romove_from_cart'),

]
