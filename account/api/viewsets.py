from django.db.models import Q
from django.contrib.auth import get_user_model
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from account.api.serializers import (
    UserCreateSerializer,
)

User = get_user_model()


class UserCreateViewSet(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
