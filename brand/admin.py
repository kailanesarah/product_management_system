from django.contrib import admin

from django.contrib import admin
from .models import Brand

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at', 'updated_at')       
    search_fields = ('name',)                                 
    list_filter = ('created_at', 'updated_at')                
    ordering = ('name',)                                      
    readonly_fields = ('created_at', 'updated_at')            

