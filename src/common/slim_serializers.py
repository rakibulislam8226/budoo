from rest_framework import serializers

from core.models import User


class UserCommonSlimSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            "uid",
            "email",
            "phone",
            "slug",
            "nid",
            "status",
        ]
