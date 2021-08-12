from django.contrib import admin
from django.urls import path

from .views import myfirstview, mysecondview

app_name = 'erp'

urlpatterns = [
    path('uno/', myfirstview, name='vista1'),
    path('dos/',mysecondview, name='vista2')
]
