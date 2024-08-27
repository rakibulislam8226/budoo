from django.contrib import admin
from .models import Attendence


# Register your models here.
# admin.site.register(Attendence)
@admin.register(Attendence)
class AttendenceAdmin(admin.ModelAdmin):
    list_display = ["user", "status"]
    search_fields = ["user__email"]
    list_filter = ["status"]
    ordering = ["-created_at"]
    readonly_fields = ["id", "uid", "created_at", "updated_at"]
    list_per_page = 50
