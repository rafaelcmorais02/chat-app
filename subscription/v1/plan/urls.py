
from .views import list_plan_view
from django.urls import path

urlpatterns = [
    path('', list_plan_view)
]
