from django.contrib import admin
from django.contrib.auth import get_user_model


class UserAcountAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "role", "full_name")
    list_display_links = ("id",)
    # list_editable = ("precio", "nombre")
    search_fields = ("id", "username")
    list_per_page = 25


admin.site.register(get_user_model(), UserAcountAdmin)
