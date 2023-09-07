from django.contrib import admin
from communication.models import FlowDefinition, FlowElement, FlowExecution, MessageElement


@admin.register(FlowDefinition)
class FlowDefinitionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'trigger', 'owner', 'created_at')


@admin.register(FlowExecution)
class FlowExecutionAdmin(admin.ModelAdmin):
    list_display = ('id', 'flow_definition', 'started_at', 'finished_at')


@admin.register(FlowElement)
class FlowElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'task_started', 'task_finished')


@admin.register(MessageElement)
class MessageElementAdmin(admin.ModelAdmin):
    list_display = ('id', 'flow_element')
