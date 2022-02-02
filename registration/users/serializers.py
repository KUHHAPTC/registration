from rest_framework import serializers

from users.models import CustomUser


class UserCreate(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ('password', 'username', 'first_name', 'last_name', 'email', )


class UserDetail(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'is_staff', 'email', 'date_joined',
                  'email_verified', )
