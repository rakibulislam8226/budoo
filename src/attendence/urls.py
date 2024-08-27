from django.urls import path

from .views import AttendenceListView

urlpatterns = [
    path("", AttendenceListView.as_view(), name="attendence-list"),
]
