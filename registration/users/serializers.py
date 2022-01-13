from django.contrib.auth.models import User
from rest_framework import serializers


class UserCreate(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('password', 'username', 'first_name', 'last_name', 'email', )


class UserDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'is_staff', 'email', 'date_joined', )
