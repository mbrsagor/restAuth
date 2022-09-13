from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .serializers import PasswordChangeSerializer
from .utils import failed_response, success_response

User = get_user_model()

FAIL_MESSAGE = 'old password is wrong'
SUCCESS_MESSAGE = 'Password changed successfully.'


class PasswordChangeAPI(generics.UpdateAPIView):
    """
    Name: User password change API
    URL: /api/user/change-password/pk/
    """
    queryset = User
    serializer_class = PasswordChangeSerializer

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response(failed_response(FAIL_MESSAGE), status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(success_response(SUCCESS_MESSAGE), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
