from django.shortcuts import render

from .forms import BookForm, AuthorForm
from .models import Book, Author
from django.http import Http404, HttpResponseRedirect, HttpResponseNotFound, HttpResponse


def index(request):
    if request.method == 'GET':
        q = request.GET.get('q')
        book_list = Book.objects.all().filter(title=q)
        len_book_list = len(book_list)
        author_list = Author.objects.all().filter(last_name=q)
        len_author_list = len(author_list)
        return render(request, 'index.html', {'book_list': book_list, 'author_list': author_list, 'len_book_list':len_book_list, 'len_author_list':len_author_list})
    else:
        return render(request, 'index.html')


def books(request):
    book_list = Book.objects.order_by('title')
    if request.method == "POST":
        if '_submit' in request.POST:
            return HttpResponseRedirect("/new_book")
    else:
        return render(request, 'books/books.html', {'book_list': book_list, 'submit_btn': 'Добавить книгу'})


def authors(request):
    author_list = Author.objects.order_by('first_name')
    if request.method == "POST":
        if '_submit' in request.POST:
            return HttpResponseRedirect("/new_author")
    else:
        return render(request, 'authors/authors.html', {'author_list': author_list, 'submit_btn': 'Добавить автора'})


def new_book(request):
    if request.method == "POST":
        book = BookForm(request.POST)

        if '_submit' in request.POST:
            if book.is_valid():
                book = Book()
                book.save()
                update_book_fields(request, book)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Invalid data")
        elif '_cancel' in request.POST:
            return HttpResponseRedirect("/")
    else:
        book_form = BookForm()
        return render(request, "books/new_book.html",
                      {"book_form": book_form, "submit_btn": "Написать"})


def new_author(request):
    if request.method == "POST":
        author = AuthorForm(request.POST)

        if '_submit' in request.POST:
            if author.is_valid():
                author = Author()
                author.save()
                update_author_fields(request, author)
                return HttpResponseRedirect("/")
            else:
                return HttpResponse("Invalid data")
        elif '_cancel' in request.POST:
            return HttpResponseRedirect("/")
    else:
        author_form = AuthorForm()
        return render(request, "authors/new_author.html",
                      {"author_form": author_form, "submit_btn": "Написать"})


def update_book_fields(request, book):
    if request.POST.get("title") is not None:
        book.title = request.POST.get("title")

    if request.POST.get("summary") is not None:
        book.summary = request.POST.get("summary")

    if request.POST.get("authors") is not None:
        book.authors.set([request.POST.get("authors")])

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


def book_update(request, book_id):
    """
    Редактирование книги
    """
    try:
        book = Book.objects.get(id=book_id)
    except book.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        book_form = BookForm(request.POST, request.FILES)

        if '_submit' in request.POST:
            if book_form.is_valid():
                try:
                    update_book_fields(request, book)
                    return HttpResponseRedirect("/books")
                except Book.DoesNotExist:
                    return HttpResponseNotFound("<h2>Post not found</h2>")
            else:
                return HttpResponse("Invalid data")
        elif '_cancel' in request.POST:
            return HttpResponseRedirect("/books")
    else:
        book_data = read_book(book)
        book_form = BookForm(book_data)
        return render(request, "books/edit_book.html",
                      {"book": book, "book_form": book_form,
                       "title": "Изменение данных", "submit_btn": "Изменить"})


def book_delete(request, book_id):
    """
    Удаление книги
    """
    try:
        book = Book.objects.get(id=book_id)
    except Book.DoesNotExist:
        raise Http404()

    book.delete()
    return HttpResponseRedirect("books/books")


def author_delete(request, author_id):
    """
    Удаление автора
    """
    try:
        author = Author.objects.get(id=author_id)
    except Author.DoesNotExist:
        raise Http404()

    author.delete()
    return HttpResponseRedirect("authors/authors")


def update_author_fields(request, author):
    if request.POST.get("first_name") is not None:
        author.first_name = request.POST.get("first_name")

    if request.POST.get("last_name") is not None:
        author.last_name = request.POST.get("last_name")

    if request.POST.get("date_of_birth") is not None:
        author.date_of_birth = request.POST.get("date_of_birth")
    author.save()


def author_update(request, author_id):
    """
    Редактирование автора
    """
    try:
        author = Author.objects.get(id=author_id)
    except author.DoesNotExist:
        raise Http404()

    if request.method == "POST":
        author_form = AuthorForm(request.POST, request.FILES)

        if '_submit' in request.POST:
            if author_form.is_valid():
                try:
                    update_author_fields(request, author)
                    return HttpResponseRedirect("/authors")
                except Author.DoesNotExist:
                    return HttpResponseNotFound("<h2>Author not found</h2>")
            else:
                return HttpResponse("Invalid data")
        elif '_cancel' in request.POST:
            return HttpResponseRedirect("/authors")
    else:
        author_data = read_author(author)
        author_form = AuthorForm(author_data)
        return render(request, "authors/edit_author.html",
                      {"author": author, "author_form": author_form,
                       "title": "Изменение данных", "submit_btn": "Изменить"})