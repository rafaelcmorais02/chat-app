
from django.urls import path
from lead.v1.lead.views import create_lead_view

urlpatterns = [
    path('', create_lead_view),
]
