from django.urls import path
from brand.views import BrandListView, BrandCreateView, BrandUpdateView, BrandDeleteView

urlpatterns = [
    path('brand/', BrandListView.as_view(), name="brand_list_view"),
    path('brand/create/', BrandCreateView.as_view(), name="brand_create_view"),
    path('brand/update/<int:pk>/', BrandUpdateView.as_view(), name="brand_update_view"),
    path('brand/delete/<int:pk>/', BrandDeleteView.as_view(), name="brand_delete_view"),
]
