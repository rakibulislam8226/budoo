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
            "uid",
            "log_type",
            "status",
            "log_data",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "uid",
            "created_at",
            "updated_at",
        ]
