from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .models import LogsTracking
from .serializers import LogTrackingListSerializer


# Create your views here.
class LogTrackingListView(generics.ListAPIView):
    queryset = LogsTracking.objects.filter()
    serializer_class = LogTrackingListSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        qs = LogsTracking.objects.filter()
        if status := self.request.query_params.get("status", None):
            status = status.lower()
            qs = qs.filter(status__iexact=status)

        return qs

class LogTrackingDetailView(generics.RetrieveAPIView):
    queryset = LogsTracking.objects.filter()
    serializer_class = LogTrackingListSerializer
    permission_classes = [IsAdminUser]
    lookup_field = "uid"