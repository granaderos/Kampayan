from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("sketch", views.sketch, name="sketch"),
    path("smart-watch", views.smart_watch, name="smart_watch"),
    path("set-time", views.set_time, name="set_time"),
    path("home", views.home, name="home"),
    path("offl", views.offline, name="offline"),
    path("create_customer", views.create_customer, name="create_customer"),
    path("login", views.login, name="login"),
    path("execute_login", views.execute_login, name="execute_login"),
    path("add_user", views.addUser, name="add_user"),
    path("add_label", views.addLabel, name="add_label"),
]