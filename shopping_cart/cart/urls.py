from django.urls import path
from .views import ShoppingCartView

app_name = 'cart'

urlpatterns = [
    path('', ShoppingCartView.as_view(), name='shopping_cart'),
]
