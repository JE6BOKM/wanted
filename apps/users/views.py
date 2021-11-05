from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from apps.core.serializers import ChooseSerializerClassMixin

from .models import User
from .serializers import CreateUserSerializer, UserSerializer


class UserViewSet(ChooseSerializerClassMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    serializer_classes = {
        "create": CreateUserSerializer,
        "update": CreateUserSerializer,
        "partial_update": CreateUserSerializer,
    }

    def get_permissions(self):
        if self.action in ["create", "update", "partial_update"]:
            self.permission_classes = [AllowAny]
        return super().get_permissions()
