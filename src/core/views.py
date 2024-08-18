from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny

from .models import User
from .serializer import UserListSerializer

# Create your views here.


class UserListView(generics.ListAPIView):
    queryset = User.objects.filter()
    serializer_class = UserListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        qs = User.objects.filter()
        if status := self.request.query_params.get("status", None):
            status = status.lower()
            qs = qs.filter(status__iexact=status)

        return qs


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserListSerializer
    permission_classes = [
        AllowAny
    ]  # TODO: Change this to IsAdminUser and request.user == self.user

    lookup_field = "email"
