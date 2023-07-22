from .views import CustomAuthToken, TesteView
from django.urls import path, include


prefix = 'user/'

urls = [
    path('token/', CustomAuthToken.as_view()),
    path('teste/', TesteView.as_view())
]

urlpatterns = [
    path(prefix, include(urls))
]
