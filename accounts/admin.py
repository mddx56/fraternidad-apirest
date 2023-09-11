from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from django.contrib import admin

from .models import UserAccount
from .forms import UserAccountChangeForm, UserAccountCreationForm


class UserAcountAdmin(admin.ModelAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = UserAccount
    list_display = (
        "id",
        "username",
        "role",
        "full_name",
        "is_staff",
        "is_active",
    )
    list_filter = (
        "username",
        "is_staff",
        "is_active",
    )
    """fieldsets = (        (None, {"fields": ("username", "password")}),        (            "Permissions",            {"fields": ("is_staff", "is_active", "groups", "user_permissions")},        ),    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                    "is_active",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )"""
    search_fields = ("username",)
    ordering = ("username",)
    list_per_page = 25


admin.site.register(UserAccount, UserAcountAdmin)
