from rest_framework.serializers import ModelSerializer
from author.models import Author


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'author', 'first_name', 'last_name', 'description']
