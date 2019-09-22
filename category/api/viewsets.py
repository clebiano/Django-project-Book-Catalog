from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from category.models import Category
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
