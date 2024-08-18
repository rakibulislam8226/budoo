from rest_framework import serializers

from .models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "uid",
            "email",
            "phone",
            "slug",
            "nid",
            "status",
            "gender",
            "date_of_birth",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "uid",
            "email",
            "phone",
            "slug",
        ]
