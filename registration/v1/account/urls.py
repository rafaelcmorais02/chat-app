
from .views import create_adm_account_view, update_account_view
from django.urls import path

urlpatterns = [
    path('adm/', create_adm_account_view),
    path('adm/<pk>', update_account_view)
]
