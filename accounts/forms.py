from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import UserAccount


class UserAccountCreationForm(UserCreationForm):
    class Meta:
        model = UserAccount
        fields = ("full_name", "suspend", "role")


class UserAccountChangeForm(UserChangeForm):
    class Meta:
        model = UserAccount
        fields = "__all__"
