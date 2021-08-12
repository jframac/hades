from django.contrib import admin
from django.urls import path

from .views import myfirstview

urlpatterns = [
    path('uno/', myfirstview),
    path('dos/',myfirstview)
]
