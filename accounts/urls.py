from django.urls import path

from accounts.views import AppLoginView, AppLogoutView, AppRegisterView

app_name = "accounts"

urlpatterns = [
    path("login", AppLoginView.as_view(), name="login"),
    path("logout", AppLogoutView.as_view(), name="logout"),
    path("register", AppRegisterView.as_view(), name="register"),
]
