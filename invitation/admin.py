from django.contrib import admin
from .models import GuestResponse, WeddingSong

@admin.register(GuestResponse)
class GuestResponseAdmin(admin.ModelAdmin):
    list_display = ['name', 'guests_count', 'attendance', 'phone', 'created_at']
    list_filter = ['attendance', 'created_at']
    search_fields = ['name', 'phone']
    readonly_fields = ['created_at']

@admin.register(WeddingSong)
class WeddingSongAdmin(admin.ModelAdmin):
    list_display = ['title', 'artist', 'is_active']
    list_editable = ['is_active']
    list_filter = ['is_active']
    search_fields = ['title', 'artist']