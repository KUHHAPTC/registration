from django.contrib.auth.models import User
from rest_framework import serializers


class UserDetail(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'password', 'username', 'first_name', 'last_name', 'is_staff', 'email', 'date_joined', )
