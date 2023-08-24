from django.contrib import admin
from .models import Lead, LeadStatus


@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone_number', 'created_at')


@admin.register(LeadStatus)
class LeadStatusAdmin(admin.ModelAdmin):
    list_display = ('id', 'lead', 'value', 'created_at')
