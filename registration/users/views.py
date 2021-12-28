from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserDetail

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        serializer = UserDetail(request.user)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


