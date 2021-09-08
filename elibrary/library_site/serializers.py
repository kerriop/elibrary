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


class RecursiveSerializer(serializers.Serializer):
    """Рекурсивный вывод для children отзывов"""

    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class FilerReviewListSerializer(serializers.ListSerializer):
    """Выводить только parents"""

    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class ReviewSerializer(serializers.ModelSerializer):
    """Вывод отзыва"""
    children = RecursiveSerializer(many=True)

    class Meta:
        list_serializer_class = FilerReviewListSerializer
        model = Review
        fields = ("name", "text", "children")


class AuthorsSerializer(serializers.ModelSerializer):
    """Вывод автора"""

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth')


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывод списка авторов"""

    class Meta:
        model = Author
        fields = ('id','first_name', 'last_name', 'date_of_birth')


class AuthorListSerializer(serializers.ModelSerializer):
    """Вывод списка авторов"""

    class Meta:
        model = Author
        fields = ('first_name', 'last_name', 'date_of_birth')


class BookAuthorsSerializer(serializers.ModelSerializer):
    """
    Вывод автора и
    преобразование списка авторов для книг из id в last_name
    """
    # authors = serializers.SlugRelatedField(slug_field="last_name", read_only=True, many=True)
    authors = AuthorListSerializer(read_only=True, many=True)
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Book
        fields = '__all__'



