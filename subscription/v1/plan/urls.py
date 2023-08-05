
from .views import PlanListAPIView
from django.urls import path

urlpatterns = [
    path('', PlanListAPIView.as_view())
]
