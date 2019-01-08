from django.contrib import admin
from django.urls import path
from .views import console_list

urlpatterns = [
    path('list/', console_list),
]
