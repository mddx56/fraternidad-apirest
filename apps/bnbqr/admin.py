from django.contrib import admin
from .models import QRRecord


# @admin.register(QRRecord)
# class QRRecordAdmin(admin.ModelAdmin):
# list_display = ("id", "currency", "amount", "gloss", "success", "created_at")
# list_filter = ("success", "currency", "created_at")
# search_fields = ("g", "additional_data", "qr_id")
# readonly_fields = "created_at"
