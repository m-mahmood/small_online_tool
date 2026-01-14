from django.contrib import admin
from .models import Advertisement

@admin.register(Advertisement)
class AdAdmin(admin.ModelAdmin):
    list_display = ('name', 'position', 'is_active', 'created_at')
    list_filter = ('position', 'is_active')