import functools

from rest_framework.response import Response


def is_email_verified():
    def _decorator(func):
        @functools.wraps(func)
        def wrapper(self, request, *args, **kwargs):
            if request.user.email_verified:
                return func(self, request, *args, *kwargs)
            else:
                return Response({"error": "You have no access rights!"})
        return wrapper

    return _decorator