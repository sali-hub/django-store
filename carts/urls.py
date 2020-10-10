from django.urls import path
from .views import add_to_cart, cart, romove_from_cart
urlpatterns = [
path('', cart,name='cart'),
path('add/<product_id>', add_to_cart,name='add_to_cart'),
path('romove_from_cart/<product_id>', romove_from_cart,name='romove_from_cart'),

]
