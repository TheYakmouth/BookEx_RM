from .models import Book
from django import forms
from django.forms import ModelForm


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = [
            'name',
            'web',
            'price',
            'picture',
        ]

