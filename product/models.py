from django.db import models
from brand.models import Brand
from category.models import Category

class Product(models.Model):
    title = models.CharField()
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='product_brand')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    description = models.TextField()
    serie_number = models.CharField()
    cost_price = models.DecimalField()
    selling_price = models.DecimalField()
    quantity = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
