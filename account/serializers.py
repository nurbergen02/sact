from rest_framework import serializers

from .models import CustomUser
from .utils import send_activation_code


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        min_length=4, required=True, write_only=True
    )
    password_confirmation = serializers.CharField(
        min_length=4, required=True,
        write_only=True
    )

    class Meta:
        model = CustomUser
        fields = (
            'email', 'password',
            'password_confirmation'
        )

    def validate(self, attrs):
        password = attrs.get('password')
        password_confirmation = attrs.pop('password_confirmation')
        if password != password_confirmation:
            msg_ = (
                "Passwords do not match"
            )
            raise serializers.ValidationError(msg_)
        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        send_activation_code(
            user.email, user.activation_code
        )
        return user


# from rest_framework import serializers
# from .models import CustomUser
# from .utils import send_activation_code
#
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(
#         min_length=4, required=True,
#         write_only=True
#     )
#
#     class Meta:
#         model = CustomUser
#         fields = (
#             "email", "password",
#             "password_confirmation"
#         )
#
#     def validate(self, attrs):
#         password = attrs.get('password')
#         password_c = attrs.pop("password_confirmation")
#         if password != password_c:
#             msg = (
#                 "Password do not match"
#             )
#             raise serializers.ValidationError("Password and password_confirmation are not the same")
#         return attrs
#
#     def create(self, validated_data):
#         user = CustomUser.objects.create_user(validated_data)
#         send_activation_code(
#             user.email, user.activation_code
#         )
#         return user
