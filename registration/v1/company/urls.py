
from .views import create_company_view
from django.urls import path

urlpatterns = [
    path('', create_company_view)
]
