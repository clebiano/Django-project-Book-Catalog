from rest_framework.serializers import ModelSerializer
from core.models import Book
from category.api.serializers import CategorySerializer
from author.api.serializers import AuthorSerializer
from review.api.serializers import ReviewSerializer

class BookSerializer(ModelSerializer):
    author = AuthorSerializer(many=True)
    category = CategorySerializer(many=True)
    review = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'description', 'author', 'category', 'comment', 'review', 'image']
