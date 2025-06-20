from django.db import models

class Brand(models.Model):
    name = models.CharField()
    description = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    
    def __str__(self):
        return self.name
    
