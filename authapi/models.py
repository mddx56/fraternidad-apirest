from django.db import models

from django.contrib.auth.models import (
    User,
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
"""

class UserAccountManager(BaseUserManager):
    def create_user(self,username, email, password=None, **extra_fields):
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()

        return user


class UserAccount(AbstractBaseUser, PermissionsMixin):
    FRATERNO = "Fraterno"
    TESORERO = "Tesorero"
    ADMIN = "Admin"
    USER_ROLE = [(FRATERNO, FRATERNO), (ADMIN, ADMIN), (TESORERO, TESORERO)]
    # username
    email = models.EmailField(max_length=255, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=10, choices=USER_ROLE, default=FRATERNO)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name", "role"]

    def get_full_name(self):
        return "{fname} {lname}".format(fname=self.first_name, lname=self.last_name)

    def get_short_name(self):
        return self.first_name

    def get_role(self):
        return self.role

    def __str__(self):
        return self.email

"""
class Notificacion(models.Model):
    titulo = models.CharField(max_length=300, default="", null=False)
    descripcion = models.TextField(default="", null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    user_destino = models.IntegerField(default=-1)
    user_remitente = models.ForeignKey(User, on_delete=models.CASCADE)
    leido = models.BooleanField(default=False)


class Token(models.Model):
    token = models.TextField(default="", null=False)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)


#class User(AbstractBaseUser):
    