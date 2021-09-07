from django import forms
from .models import Author, Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'authors', 'summary', 'genre', 'image']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "title"}),
            'authors': forms.CheckboxSelectMultiple(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "authors"}),
            'summary': forms.Textarea(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "summary"}),
            'genre': forms.TextInput(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "genre"}),
            'image': forms.FileInput(attrs={
                "id": "input_file", 'type': "file", "opacity": "0",
                "visibility": "hidden", "position": "absolute"}),
        }


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "first_name"}),
            'last_name': forms.TextInput(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "last_name"}),
            'date_of_birth': forms.DateInput(attrs={
                'class': "wicon", "id": "title", 'type': "text",
                'placeholder': "2021-09-04"}),
        }
