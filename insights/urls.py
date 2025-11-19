from django.urls import path
from .views import LossSummaryView

urlpatterns = [
    path('loss-summary/', LossSummaryView.as_view()),
]
