from django.contrib import admin
from django.urls import path

from core.erp.views.category.views import CategoryListView

app_name = 'erp'

urlpatterns = [
    path('category/list/', CategoryListView.as_view(), name='category_list'),
]
