
from .views import CompanyAPIView
from django.urls import path


urlpatterns = [
    path('', CompanyAPIView.as_view())
]
