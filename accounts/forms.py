from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import UserAccount


class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ("__all__")


class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = ("__all__")
