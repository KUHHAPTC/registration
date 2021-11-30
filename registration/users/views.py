from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import GetAllUserInfo


class CheckUser(APIView):

    def get(self, request):
        users = User.objects.all()
        serializer = GetAllUserInfo(users, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
