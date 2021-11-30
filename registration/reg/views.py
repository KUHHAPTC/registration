from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from users.serializers import GetAllUserInfo


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = User.objects.get(username=request.user.username)
        serializer = GetAllUserInfo(user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


class CreateUser(APIView):

    def post(self, request):
        serializer = GetAllUserInfo(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
