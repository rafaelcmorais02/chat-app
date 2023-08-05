from django.urls import path, include

urlpatterns = [
    path('v1/plans/', include('subscription.v1.plan.urls')),
]
