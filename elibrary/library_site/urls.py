from django.urls import path
from . import views

# app_name = 'library_site'
# pattern_name = 'library_site'

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
    # path("searchbar/", views.searchbar, name='searchbar'),
    # path("search/", views.Search.as_view(), name='search'),


    # path('search', views.book_list, name='book_list'),
    # path('search/', views.book_detail, name='book_detail'),
    # path('search/search/', views.search, name='search'),
]
