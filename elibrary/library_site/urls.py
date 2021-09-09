from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("", views.index, name='index'),
    path("authors/", views.authors, name='authors'),
    path("books/", views.books, name='books'),
    path("book_update/<int:book_id>/", views.book_update),
    path("book_delete/<int:book_id>/", views.book_delete),
    path("author_update/<int:author_id>/", views.author_update),
    path("author_delete/<int:author_id>/", views.author_delete),
    path("new_book/", views.new_book),
    path("new_author/", views.new_author),

    # path('api/v1/book/', views.BookListView.as_view()),
    path('api/v1/book/', api.BookViewSet.as_view({'get': 'list'})),
    # path('api/v1/book/<int:pk>', views.BookAuthorView.as_view()),
    path('api/v1/book/<int:pk>', api.BookViewSet.as_view({'get': 'retrieve'})),
    path('api/v1/review/', views.ReviewCreateView.as_view()),

    path('api/v1/author/', views.AuthorListView.as_view()),
    path('api/v1/author/<int:pk>', views.AuthorView.as_view()),
]
