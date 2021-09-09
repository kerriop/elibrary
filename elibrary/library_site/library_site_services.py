from django_filters import rest_framework as filters
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .models import Book


def update_book_fields(request, book):
    if request.POST.get("title") is not None:
        book.title = request.POST.get("title")

    if request.POST.get("summary") is not None:
        book.summary = request.POST.get("summary")

    if request.POST.get("authors") is not None:
        list = request.POST.getlist('authors')
        book.authors.set('')
        for item in list:
            book.authors.add(item)

    if request.POST.get("genre") is not None:
        book.genre = request.POST.get("genre")

    if request.FILES.get("image") is not None:
        book.image = request.FILES.get("image")
    book.save()


def read_book(book):
    ret = {'title': book.title,
           'summary': book.summary,
           'authors': book.authors,
           'genre': book.genre,
           'image': book.image}
    return ret


def read_author(author):
    ret = {'first_name': author.first_name,
           'last_name': author.last_name,
           'date_of_birth': author.date_of_birth}
    return ret


def update_author_fields(request, author):
    if request.POST.get("first_name") is not None:
        author.first_name = request.POST.get("first_name")

    if request.POST.get("last_name") is not None:
        author.last_name = request.POST.get("last_name")

    if request.POST.get("date_of_birth") is not None:
        author.date_of_birth = request.POST.get("date_of_birth")
    author.save()


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class BookFilter(filters.FilterSet):
    # genre = CharFilterInFilter(field_name='book__genre', lookup_expr='in')
    authors = CharFilterInFilter(field_name='authors__id', lookup_expr='in')

    class Meta:
        model = Book
        fields = ['authors']


class PaginationAuthors(PageNumberPagination):
    page_size = 2
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response({
            'links': {
                'next': self.get_next_link(),
                'previous': self.get_previous_link()
            },
            'count': self.page.paginator.count,
            'results': data
        })
