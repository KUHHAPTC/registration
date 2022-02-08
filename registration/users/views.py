from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserDetail
from users.functions import is_email_verified



class UserMeView(APIView):
    permission_classes = (IsAuthenticated,)

    @is_email_verified()
    def get(self, request):
        return Response(status=status.HTTP_200_OK, data=UserDetail(request.user).data)
