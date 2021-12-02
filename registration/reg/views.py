from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserDetail


class CreateUser(APIView):

    def post(self, request):
        serializer = UserDetail(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
