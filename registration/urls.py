from django.urls import path, include

urlpatterns = [
    path('v1/companies/', include('registration.v1.company.urls')),
    path('v1/accounts/', include('registration.v1.account.urls')),
]
