from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import get_object_or_404
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from users.serializers import UserCreateSerializer
from users.models import CustomUser
from .tasks import task_send_mail


class CreateUser(APIView):

    def post(self, request):
        serializer = UserCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = CustomUser.objects.create_user(**serializer.data)
        token = default_token_generator.make_token(user)
        uid64 = urlsafe_base64_encode(force_bytes(user.pk))
        task_send_mail.delay(request.build_absolute_uri(), uid64, token, user.email)
        return Response(status=status.HTTP_201_CREATED,
                        data={'info': f'We send activation link on {user.email}'})


class VerifyEmail(APIView):

    def get(self, request, uid64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid64))
            user = get_object_or_404(klass=CustomUser, pk=uid)
            if not default_token_generator.check_token(user, token):
                raise ValueError
        except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
            return Response({'error': 'Activation link is invalid!'})

        user.email_verified = True
        user.save(update_fields=["email_verified"])
        return Response(status=status.HTTP_200_OK,
                        data={'info': f'Successfully verified! Now you can close this tab or '
                                      f'follow {request.build_absolute_uri("/api/users/me/")}'})
