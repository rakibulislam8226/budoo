from django.urls import path

from .views import LogTrackingListView, LogTrackingDetailView

urlpatterns = [
    path("/<uuid:uid>", LogTrackingDetailView.as_view(), name="logs-details"),
    path("", LogTrackingListView.as_view(), name="logs-list"),
]
