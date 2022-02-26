from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserDetailSerializer
from users.permissions import IsEmailVerified


class UserMeView(APIView):
    permission_classes = (IsAuthenticated, IsEmailVerified)

    def get(self, request):
        return Response(status=status.HTTP_200_OK, data=UserDetailSerializer(request.user).data)
