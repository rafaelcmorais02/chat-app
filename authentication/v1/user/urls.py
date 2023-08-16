from .views import CustomAuthToken, password_redefinition_view
from django.urls import path

urlpatterns = [
    path('token/', CustomAuthToken.as_view()),
    path('password/redefinition/', password_redefinition_view)
]
