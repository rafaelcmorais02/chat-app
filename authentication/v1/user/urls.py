from .views import CustomAuthToken
from django.urls import path

urlpatterns = [
    path('token/', CustomAuthToken.as_view()),
]
