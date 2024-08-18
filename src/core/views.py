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


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.filter()
    serializer_class = UserListSerializer
    permission_classes = [
        AllowAny
    ]  # TODO: Change this to IsAdminUser and request.user == self.user

    lookup_field = "email"
