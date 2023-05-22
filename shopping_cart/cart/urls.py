from django.contrib.auth.decorators import login_required
from django.urls import path

from .views import ShoppingCartView, LoginView, RegistrationView, LogoutView

app_name = "cart"

urlpatterns = [
    path("", login_required(ShoppingCartView.as_view()), name="shopping_cart"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("register/", RegistrationView.as_view(), name="register"),
]
