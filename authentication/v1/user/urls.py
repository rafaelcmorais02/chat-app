from .views import CustomAuthTokenView, password_redefinition_view
from django.urls import path

urlpatterns = [
    path('token/', CustomAuthTokenView.as_view()),
    path('password/redefinition/', password_redefinition_view)
]
