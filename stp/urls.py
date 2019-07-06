from django.urls import path
from . import views

urlpatterns = [
    path("add_user", views.addUser, name="add_user"),
    path("add_label", views.addLabel, name="add_label"),
]