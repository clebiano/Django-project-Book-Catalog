from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from author.models import Author
from .serializers import AuthorSerializer


class AuthorViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
