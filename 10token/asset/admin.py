from django.contrib import admin
from .models import Asset, Waves

@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display = ('name','amount','token_id','created_date')
    list_filter = ('reissuable',)
    search_fields = ('name','amount','token_id','created_date')


@admin.register(Waves)
class WavesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Waves._meta.fields]
