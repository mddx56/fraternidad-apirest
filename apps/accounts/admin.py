from django.contrib import admin
from .models import UserAccount
from .forms import UserAccountChangeForm, UserAccountCreationForm


@admin.action(description="Suspender Fraterno")
def suspend_user(modeladmin, request, queryset):
    queryset.update(suspend=True)


@admin.action(description="Activar Fraterno")
def activated_user(modeladmin, request, queryset):
    queryset.update(suspend=False)


class UserAcountAdmin(admin.ModelAdmin):
    add_form = UserAccountCreationForm
    form = UserAccountChangeForm
    model = UserAccount

    def username_ci(self, obj):
        return obj.username

    username_ci.short_description = "Ci"

    def get_actions(self, request):
        actions = super().get_actions(request)
        if "delete_selected" in actions:
            del actions["delete_selected"]
        return actions

    actions = [suspend_user, activated_user]

    list_display = (
        "username_ci",
        # "username",
        "full_name",
        "role",
        "suspend",
        # "is_active",
    )
    list_filter = (
        "role",
        "suspend",
        # "is_active",
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
    search_fields = (
        "id",
        "username",
        "full_name",
    )
    ordering = ("full_name",)


admin.site.register(UserAccount, UserAcountAdmin)
