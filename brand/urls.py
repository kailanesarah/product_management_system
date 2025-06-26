from django.urls import path
from django.shortcuts import render
from brand.views import BrandListView

urlpatterns = [
    path('brand/', BrandListView.as_view(), name="brand_list_view" ),
]
