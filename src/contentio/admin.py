from django.contrib import admin
from .models import LogsTracking

# Register your models here.


@admin.register(LogsTracking)
class LogsTrackingAdmin(admin.ModelAdmin):
    list_display = ["log_type", "created_at", "status"]
    list_filter = ["log_type"]
    readonly_fields = ["uid", "created_at", "updated_at"]
    date_hierarchy = "created_at"
    list_per_page = 50
