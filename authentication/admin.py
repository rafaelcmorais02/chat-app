from django.contrib import admin
from .models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'email', 'is_superuser', 'is_active')
