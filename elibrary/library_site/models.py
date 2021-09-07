from django.db import models

from django.urls import reverse


def book_directory_path(instance, filename):
    return f"book_{instance.id}/{filename}"


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(null=True, blank=True)
    # url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return f"{self.last_name}, {self.first_name}"

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={"slug": self.last_name})


class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author, blank=True)
    summary = models.TextField(max_length=1000)
    genre = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=False, default='default/default.jpg',
                              upload_to=book_directory_path)
    # url = models.SlugField(max_length=130, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book_detail', kwargs={"slug": self.title})

    class Meta:
        ordering = ['id']
