from django.db import models
from product.models import Product

class Inflow(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='inflow_product')
    quantity = models.IntegerField()
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
        
    
