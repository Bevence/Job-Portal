from django.urls import path
from accounts.views import UserRegistrationView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path("register/", UserRegistrationView.as_view(), name = "user_register"),
]
