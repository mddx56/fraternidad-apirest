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
        # extra_fields.setdefault("is_staff", False)
        # extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password=None, **extra_fields):
        user = self._create_user(username, email, password, **extra_fields)
        # extra_fields.setdefault("is_superuser", True)
        
        user.is_superuser = True
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

    NORMAL = "normal"
    PLANPAGOS = "plan"
    FINANCIAL = [(NORMAL, "Normal"), (PLANPAGOS, "Plan de Pagos")]
    USER_ROLE = [(FRATERNO, "fraterno"), (ADMIN, "admin"), (TESORERO, "tesorero")]
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
    email = models.EmailField(max_length=150, unique=True)
    phone = models.CharField(max_length=15, blank=True, null=True, default="")
    financial_condition = models.CharField(
        max_length=17, choices=FINANCIAL, default=NORMAL
    )
    role = models.CharField(max_length=15, choices=USER_ROLE, default=FRATERNO)
    copy_ci = models.BooleanField(default=False)
    avatar = models.BooleanField(default=False)
    active = models.BooleanField(default=True)
    suspend = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    admin = models.BooleanField(default=False)
    verified = models.BooleanField(default=False)

    objects = CustomUserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["full_name", "email"]

    def get_role(self):
        return self.role

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

    def __str__(self) -> str:
        return f"User : {self.full_name}"
