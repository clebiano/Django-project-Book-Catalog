from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from core.models import Book
from .serializers import BookSerializer


class BookViewSet(ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    permission_classes = [IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    # queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'category__category']

    def get_queryset(self):
        id = self.request.query_params.get('id', None)
        title = self.request.query_params.get('title', None)
        # category = self.request.query_params.get('category', None)
        queryset = Book.objects.all()
        if id:
            queryset = Book.objects.filter(pk=id)
        if title:
            queryset = queryset.filter(title__iexact=title)
        # if category:
        #     queryset = queryset.filter(category__iexact=category)
        return queryset

    # def list(self, request, *args, **kwargs):
    #     return Response({"title": 123})

    # def create(self, request, *args, **kwargs):
    #     return Response({'Hello': request.data['name']})

    # def destroy(self, request, *args, **kwargs):
    #     pass

    # def retrieve(self, request, *args, **kwargs):
    #     pass

    # def update(self, request, *args, **kwargs):
    #     pass

    # def partial_update(self, request, *args, **kwargs):
    #     pass

    # @action(methods=['get'], detail=True)
    # def alert(self, request, pk=None):
    #     pass
