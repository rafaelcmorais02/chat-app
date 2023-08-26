
from django.urls import path, include

urlpatterns = [
    path('v1/flow_definitions/', include('communication.v1.flow_definition.urls')),
]
