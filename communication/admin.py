from django.contrib import admin
from communication.models import FlowDefinition


@admin.register(FlowDefinition)
class FlowDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'trigger', 'owner', 'created_at')
