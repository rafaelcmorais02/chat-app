from django.contrib import admin
from .models import Company, Account


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'phone_number')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'is_company_admin', 'is_company_staff')
    exclude = ('full_name', 'is_superuser', 'is_staff')
