from django.contrib import admin
from .models import Profile, Address


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'date_of_birth', 'created_at')
    search_fields = ('user__username', 'phone')
    list_filter = ('created_at',)
    ordering = ('-created_at',)


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('user', 'full_name', 'city', 'district', 'is_default', 'created_at')
    search_fields = ('full_name', 'city', 'district')
    list_filter = ('city', 'is_default', 'created_at')
    ordering = ('-created_at',)
