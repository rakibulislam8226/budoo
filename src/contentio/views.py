from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import LogsTracking
from .serializers import LogTrackingListSerializer


# Create your views here.
class LogTrackingListView(generics.ListAPIView):
    serializer_class = LogTrackingListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = LogsTracking.objects.order_by("-created_at")
        if status := self.request.query_params.get("status", None):
            status = status.lower()
            qs = qs.filter(status__iexact=status)

        return qs


class LogTrackingDetailView(generics.RetrieveAPIView):
    queryset = LogsTracking.objects.filter().order_by("created_at")
    serializer_class = LogTrackingListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "uid"
