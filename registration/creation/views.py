from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserCreate


class CreateUser(APIView):

    def post(self, request):
        serializer = UserCreate(data=request.data)
        serializer.is_valid(raise_exception=True)
        User.objects.create_user(**serializer.data)
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
