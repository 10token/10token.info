from django.contrib import admin
from .models import Asset

class AssetAdmin(admin.ModelAdmin):
    list_display = ('name','amount','token_id','created_date')
    list_filter = ('reissuable',)
    search_fields = ('name','amount','token_id','created_date')

admin.site.register(Asset, AssetAdmin)
