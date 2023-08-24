from django.contrib import admin
from .models import Company, Account


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cnpj', 'phone_number', 'created_at')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'cpf', 'is_company_admin', 'is_company_staff', 'created_at')
    exclude = ('full_name', 'is_superuser', 'is_staff')
