from django.urls import path

from .views import UserListView, UserDetailView

urlpatterns = [
    path("users", UserListView.as_view(), name="user-list"),
    path("users/<str:email>", UserDetailView.as_view(), name="user-detail"),
]
