from rest_framework import generics, status, views
from rest_framework.response import Response
from django.contrib.auth import get_user_model

from .permissions import AuthorOrReadOnly
from .utils import failed_response, success_response
from .serializers import PasswordChangeSerializer, ProfileSerializer
from .response import prepare_success_response, prepare_error_response
from .messages import ID_NOT_FOUND, SUCCESS_MESSAGE, WRONG_MESSAGE, REMOVE_USER, CANCEL_USER

User = get_user_model()


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
                return Response(failed_response(), status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            return Response(success_response(SUCCESS_MESSAGE), status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Profile(views.APIView):
    permission_classes = (AuthorOrReadOnly,)

    """
       Name: User Profile API for Web mobile both
       URL: /api/v1/user/profile/
    """

    def get(self, request, **kwargs):
        try:
            user = User.objects.get(id=self.request.user.id)
            if user is not None:
                serializer = ProfileSerializer(user)
                return Response(success_response(serializer.data), status=status.HTTP_200_OK)
            return Response(failed_response(ID_NOT_FOUND), status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(failed_response(str(ex)), status=status.HTTP_200_OK)


class ProfileUpdateAPIView(generics.UpdateAPIView):
    """
    User profile update API
    :param
    id
    """

    def put(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile is not None:
            serializer = ProfileSerializer(profile, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=self.request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(failed_response(serializer.errors), status=status.HTTP_400_BAD_REQUEST)
        return Response(failed_response(WRONG_MESSAGE), status=status.HTTP_200_OK)


class DeleteUserAPIView(views.APIView):
    def delete(self, reqeust, pk):
        try:
            action = reqeust.data.get('action')  # Action get from reqeust
            member = User.objects.get(id=pk)
            if member is not None:
                if action == 1:
                    member.delete()
                    return Response(prepare_success_response(REMOVE_USER), status=status.HTTP_200_OK)
                if action == 2:
                    member.delete()
                    return Response(prepare_success_response(CANCEL_USER), status=status.HTTP_200_OK)
            return Response(prepare_error_response(ID_NOT_FOUND), status=status.HTTP_400_BAD_REQUEST)
        except Exception as ex:
            return Response(prepare_error_response(str(ex)), status=status.HTTP_404_NOT_FOUND)
