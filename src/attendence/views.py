from rest_framework import generics

from rest_framework.permissions import IsAuthenticated
from common.permissions import IsOwner

from .models import Attendence
from .serializers import AttendenceListSerializer

# Create your views here.


class AttendenceListView(generics.ListCreateAPIView):
    serializer_class = AttendenceListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Attendence.objects.select_related("user").filter(user=self.request.user)
