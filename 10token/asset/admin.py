from django.contrib import admin
from .models import Asset, AssetTop

class AssetTopInline(admin.StackedInline):
    model = AssetTop

class AssetAdmin(admin.ModelAdmin):
    list_display = ('name','amount','token_id','created_date')
    list_filter = ('reissuable',)
    search_fields = ('name','amount','token_id','created_date')
    inlines = [AssetTopInline]

admin.site.register(Asset, AssetAdmin)
