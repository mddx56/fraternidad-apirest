from django.conf import settings
from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserFraterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "full_name", "email", "phone")


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token["username"] = user.username
        token["ci"] = user.ci
        token["name"] = user.full_name
        token["role"] = user.role
        token["email"] = user.email
        token["phone"] = user.phone
        token["avatar"] = user.avatar
        token["suspend"] = user.suspend
        token["active"] = user.is_active
        # token["id"] = str(user.id)
        return token


class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True  # , validators=[password_validation]
    )
    password2 = serializers.CharField(write_only=True, required=True)
    old_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ("old_password", "password", "password2")

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "Password no son iguales."})
        return attrs

    def validate_old_password(self, value):
        user = self.context["request"].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Password es incorrecto"}
            )
        return value

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class UpdateUserSerializer(serializers.ModelSerializer):
    # email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "full_name", "email", "phone")
        extra_kwargs = {
            "full_name": {"required": True},
        }

    def validate_email(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(email=value).exists():
            raise serializers.ValidationError({"email": "ya existe este email"})
        return value

    def validate_username(self, value):
        user = self.context["request"].user
        if User.objects.exclude(pk=user.pk).filter(username=value).exists():
            raise serializers.ValidationError(
                {"username": "Este nombre de usuario ya existe"}
            )
        return value

    def update(self, instance, validated_data):
        instance.full_name = validated_data["full_name"]
        instance.email = validated_data["email"]
        instance.username = validated_data["username"]
        instance.phone = validated_data["phone"]

        instance.save()

        return instance


class UuIdSerializer(serializers.Serializer):
    id = serializers.UUIDField()

    def validate_id(self, value):
        if not value:
            raise serializers.ValidationError("No valido..")
        return value
