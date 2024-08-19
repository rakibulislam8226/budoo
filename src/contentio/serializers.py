from rest_framework import serializers

from .models import LogsTracking


class LogTrackingListSerializer(serializers.ModelSerializer):
    """
    Serializer for LogsTracking model.
    """

    class Meta:
        model = LogsTracking
        fields = [
            "id",
            "log_type",
            "status",
            "log_data",
            "created_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
