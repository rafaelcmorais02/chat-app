from django.urls import path, include

urlpatterns = [
    path('v1/leads/', include('lead.v1.lead.urls')),
]
