from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreationForm
    form = UserChangeForm
    model = User
    list_display = [
        "phone",
        "uid",
        "status",
        "email",
        "slug",
    ]
    list_filter = UserAdmin.list_filter + ("status",)
    ordering = ("-date_joined",)
    fieldsets = UserAdmin.fieldsets + (
        (
            "Extra Fields",
            {
                "fields": (
                    "phone",
                    "gender",
                    "status",
                    "date_of_birth",
                    "nid",
                )
            },
        ),
    )
    add_fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "phone",
                )
            },
        ),
    ) + UserAdmin.add_fieldsets
