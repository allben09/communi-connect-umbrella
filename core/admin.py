from django.contrib import admin
from .models import Organization, Donation, ContactMessage


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'province', 'is_active', 'created_at')
    list_filter = ('category', 'province', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active',)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('donor_name', 'amount', 'currency', 'organization', 'created_at')
    list_filter = ('currency', 'created_at')
    search_fields = ('donor_name', 'donor_email')


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'created_at')
    search_fields = ('name', 'email', 'subject')
