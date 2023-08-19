import uuid
from django.db import models
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("falta el username..")
        if not email:
            raise ValueError("falta el email..")
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self._create_user(username, email, password, **extra_fields)
        user.admin = True
        user.staff = True
        user.role = "admin"
        user.verified = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    FRATERNO = "Fraterno"
    TESORERO = "Tesorero"
    ADMIN = "Admin"
    username_validator = UnicodeUsernameValidator()
    USER_ROLE = [(FRATERNO, "fraterno"), (ADMIN, "admin"), (TESORERO, "tesorero")]
    username = models.CharField(
        max_length=255,
        validators=[username_validator],
        unique=True,
        error_messages={
            "unique": "Un usuario con es nombre ya existe.",
        },
    )
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    first_name = models.CharField(max_length=155)
    last_name = models.CharField(max_length=155)
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=15)
    avatar = models.CharField(max_length=100, null=True, default="")
    role = models.CharField(max_length=15, choices=USER_ROLE, default=FRATERNO)
    active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "role"]

    def get_full_name(self):
        return f"nombres= {self.first_name}, apellidos= {self.last_name}"

    def get_short_name(self):
        return self.first_name

    def get_role(self):
        return self.role

    def __str__(self):
        return self.email

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
