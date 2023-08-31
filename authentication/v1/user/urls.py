from .views import CustomAuthTokenView, password_redefinition_view, google_auth_view, social_auth
from django.urls import path

urlpatterns = [
    path('token/', CustomAuthTokenView.as_view()),
    path('password/redefinition/', password_redefinition_view),
    path('auth-google/', google_auth_view),
    path('social-auth/', social_auth)
]
