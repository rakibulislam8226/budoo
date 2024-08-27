from rest_framework import generics

from rest_framework.permissions import IsAuthenticated

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


from common.permissions import IsOwner

from .models import Attendence
from .serializers import AttendenceListSerializer

# Create your views here.


class AttendenceListView(generics.ListCreateAPIView):
    serializer_class = AttendenceListSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Attendence.objects.select_related("user").filter(user=self.request.user)

    def perform_create(self, serializer):
        instance = serializer.save()
        self.notify_websocket(instance)

    def notify_websocket(self, instance):
        channel_layer = get_channel_layer()
        async_to_sync(channel_layer.group_send)(
            "status_updates",
            {
                "type": "status_update",
                "status": instance.status,
                "user": instance.user.username,
            },
        )
