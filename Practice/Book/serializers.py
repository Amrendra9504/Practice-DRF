from rest_framework import serializers

from Book.models import Author, Publisher, Book
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.name', read_only=True)
    publisher_name = serializers.CharField(source='publisher.name', read_only=True)

    class Meta:
        model = Book
        fields = ['id', 'title', 'publication_date', 'author', 'publisher', 'author_name', 'publisher_name']
