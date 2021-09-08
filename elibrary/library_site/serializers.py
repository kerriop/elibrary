from rest_framework import serializers

from .models import Book, Author, Review


class BookListSerializer(serializers.ModelSerializer):
    """Вывод списка книг"""

    class Meta:
        model = Book
        fields = ('title', 'authors', 'summary', 'genre', 'image')


class ReviewCreateSerializer(serializers.ModelSerializer):
    """Добавление отзыва"""

    class Meta:
        model = Review
        fields = "__all__"


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""

    class Meta:
        model = Review
        fields = ("name", "text", "parent")


class BookAuthorsSerializer(serializers.ModelSerializer):
    """
    Вывод автора и
    преобразование списка авторов для книг из id в last_name
    """
    authors = serializers.SlugRelatedField(slug_field="last_name", read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывод списка авторов"""

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth')


class AuthorsSerializer(serializers.ModelSerializer):
    """Вывод автора"""

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth')
