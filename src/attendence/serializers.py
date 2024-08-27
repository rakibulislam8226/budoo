from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from common.slim_serializers import UserCommonSlimSerializer

from .models import Attendence


class AttendenceListSerializer(serializers.ModelSerializer):
    user = UserCommonSlimSerializer(read_only=True)

    class Meta:
        model = Attendence
        fields = ["id", "uid", "user", "status", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "uid", "created_at", "updated_at"]

    def validate(self, attrs):
        request = self.context["request"]
        user = request.user
        new_status = attrs.get("status")

        if (
            Attendence.objects.select_related("user")
            .filter(user=user, status=new_status)
            .exists()
        ):
            raise ValidationError(
                {
                    "status": [
                        "You cannot select the same status that you are already in."
                    ]
                }
            )

        return super().validate(attrs)

    def create(self, validated_data):
        request = self.context["request"]
        user = request.user
        new_status = validated_data.get("status")
        if (
            existing_attendance := Attendence.objects.select_related("user")
            .filter(user=user)
            .first()
        ):
            existing_attendance.status = new_status
            existing_attendance.save()

            return existing_attendance
        else:
            validated_data["user"] = user
            new_attendance = super().create(validated_data)
            return new_attendance
