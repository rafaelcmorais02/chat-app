
from django.urls import path
from communication.v1.flow_definition.views import create_definition_view


urlpatterns = [
    path('', create_definition_view),
]
