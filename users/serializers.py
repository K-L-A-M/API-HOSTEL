from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework.validators import UniqueValidator
from rooms.serializers import RoomSerializer
from users.models import TypeUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(format='hex', read_only=True)
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(validators=[
        UniqueValidator(
            queryset=User.objects.all(),
            message="A user with this email already exists.",
        )
    ])
    password = serializers.CharField(write_only=True)
    contact = serializers.CharField(max_length=15)
    cpf = serializers.CharField(max_length=14, validators=[
        UniqueValidator(
            queryset=User.objects.all(),
            message="A user with this cpf already exists.",
        )
    ])
    nationality = serializers.CharField(max_length=50, required=False,)
    emergency_contact = serializers.CharField(max_length=15, required=False, allow_blank=True)
    favorite_rooms = RoomSerializer(many=True, read_only=True)
    type_user = serializers.ChoiceField(choices=TypeUser.choices)

    def create(self, validated_data: dict) -> User:
        type_user = validated_data.get("type_user", TypeUser.USER)

        if type_user == TypeUser.ADMIN:
            return User.objects.create_superuser(**validated_data)
        else:
            return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            if key == "password":
                instance.set_password(value)
            else:
                setattr(instance, key, value)

        if not self.partial:
            instance.save()

        favorite_rooms_data = validated_data.pop('favorite_rooms', None)

        instance = super().update(instance, validated_data)

        if favorite_rooms_data is not None:
            instance.favorite_rooms.set(favorite_rooms_data)

        return instance

    def format_cpf(self, value):
        if value and len(value) == 11:
            return f"{value[:3]}.{value[3:6]}.{value[6:9]}-{value[9:]}"
        return value

    def format_contact(self, value):
        if value and len(value) >= 10:
            return f"({value[:2]}) {value[2:6]}-{value[6:]}"
        return value

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "name",
            "contact",
            "cpf",
            "nationality",
            "emergency_contact",
            "favorite_rooms",
            "type_user",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "favorite_rooms": {"read_only": True}
        }

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['cpf'] = self.format_cpf(representation.get('cpf', ''))
        representation['contact'] = self.format_contact(representation.get('contact', ''))
        return representation


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        user = self.user
        user_serializer = UserSerializer(user)  # Use seu serializer existente
        data['user'] = user_serializer.data
        return data
