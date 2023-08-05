from .views import CustomAuthToken, TesteView
from django.urls import path

urlpatterns = [
    path('token/', CustomAuthToken.as_view()),
    path('teste/', TesteView.as_view())
]
