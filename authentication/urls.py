from django.urls import path, include

urlpatterns = [
    path('v1/users/', include('authentication.v1.user.urls')),
]
