from django.contrib import admin
from django.urls import path
from .views import home_func, valorant_func, overwatch_func

urlpatterns = [
    path("", home_func, name="home"),
    path("valorant/", valorant_func, name="valorant"),
    path("overwatch/", overwatch_func, name="overwatch"),
]
