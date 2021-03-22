from rest_framework import viewsets, mixins, generics, status
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import User
from .serializers import UserSerializer, UserRegisterSerializer


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = User
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    @action(methods=['GET'], detail=True, url_name='user-activity',
            permission_classes=[permissions.IsAuthenticated])
    def user_activity(self, request, pk=None):
        user = User.objects.filter(pk=pk).first()

        if not user:
            return Response({'error': 'Invalid user id!'}, status=status.HTTP_400_BAD_REQUEST)

        return Response({'last-login': request.user.last_login, 'last-activity': request.user.last_activity})


class CreateUserView(generics.CreateAPIView):
    model = User
    serializer_class = UserRegisterSerializer
