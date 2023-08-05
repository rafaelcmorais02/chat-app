
from .views import AdmAccountAPIView
from django.urls import path

urlpatterns = [
    path('adm/', AdmAccountAPIView.as_view()),
]
