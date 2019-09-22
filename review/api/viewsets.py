from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from review.models import Review
from .serializers import ReviewSerializer


class ReviewViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
