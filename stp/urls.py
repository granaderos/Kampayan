from django.urls import path
from . import views

urlpatterns = [
    path("users/", views.users, name="users"),
    path("add_user", views.addUser, name="add_user"),
    path("add_merchant", views.addMerchant, name="add_merchant")
]