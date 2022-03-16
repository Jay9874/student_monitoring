from . import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logut", views.logout_view, name="logout"),
    path("forgot", views.forgot, name="forgot")
]

