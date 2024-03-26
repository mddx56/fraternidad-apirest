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
        user.save(using=self._db)

        return user

    def create_user(self, username, email, password=None, **extra_fields):
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_superuser", False)-/

        user = self._create_user(username, email, password, **extra_fields)
        user.is_superuser = False
        user.is_admin = False
        user.is_staff = False
        user.is_active = True
        user.verified = True
        user.save()
        return user

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self._create_user(username, email, password, **extra_fields)
        # extra_fields.setdefault("is_admin", True)
        # extra_fields.setdefault("is_superuser", True)

        user.is_superuser = True
        user.is_admin = True
        user.is_staff = True
        user.is_active = True
        user.role = "Admin"
        user.verified = True
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    FRATERNO = "Fraterno"
    TESORERO = "Tesorero"
    ENCARGADO = "Encargado"
    ADMIN = "Admin"
    username_validator = UnicodeUsernameValidator()

    NORMAL = "Normal"
    PLANPAGOS = "Plan de Pagos"
    FINANCIAL = [(NORMAL, "normal"), (PLANPAGOS, "plan")]
    USER_ROLE = [(FRATERNO, "fraterno"), (ADMIN, "admin"), (TESORERO, "tesorero"),(ENCARGADO,"encargado")]
    username = models.CharField(
        max_length=255,
        validators=[username_validator],
        unique=True,
        error_messages={
            "unique": "Nombre de usuario o CI ya existe.",
        },
    )

    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    ci = models.BooleanField(default=False)
    full_name = models.CharField(max_length=355, null=False, default="")
    email = models.EmailField(max_length=150, blank=True, null=True)
    phone = models.CharField(max_length=15, blank=True, null=True, default="")
    financial_condition = models.CharField(
        max_length=17, choices=FINANCIAL, default=NORMAL
    )
    role = models.CharField(max_length=15, choices=USER_ROLE, default=FRATERNO)
    copy_ci = models.BooleanField(default=False)
    avatar = models.BooleanField(default=False)
    suspend = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "email"]

    def get_role(self):
        return self.role

    def has_module_perms(self, app_label):
        return True

    def __str__(self) -> str:
        return f"User : {self.full_name}, {self.ci}, {self.username}"
