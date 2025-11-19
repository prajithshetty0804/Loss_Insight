from django.urls import path
from .views import WeeklyLossAPIView

urlpatterns = [
    path('weekly-loss/', WeeklyLossAPIView.as_view(), name='weekly-loss'),
]
