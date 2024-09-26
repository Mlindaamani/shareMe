from django import forms
from .models import Book
from django.forms import ModelForm


class BookForm(ModelForm):

    class Meta:
        model = Book
        fields = ['name', 'price', 'description', 'image', 'category', 'isbin']

        widgets = {
            'description': forms.Textarea(attrs={"cols": 10, "rows": 5}),
            'name': forms.TextInput(attrs={'class': 'p-2 fw-bolder'}),
            'category': forms.SelectMultiple(attrs={'class': 'form-select p-2 form-select-sm '})
        }


class EmailBookForm(forms.Form):
    name = forms.CharField(
        max_length=64,
        min_length=5,
        disabled=True,
        label='YOUR NAME',
        widget=forms.TextInput(
            attrs={'class': 'fw-bold p-3 form-control text-dark'}
        )
    )

    to = forms.EmailField(
        required=True,
        max_length=100,
        min_length=10,
        label='RECIPIENT-EMAIL',
        help_text="Enter your email here...",
        widget=forms.TextInput(attrs={
            'class': 'fw-bolder p-3 form-control'
        })
    )

    comment = forms.CharField(
        label="COMMENT",
        help_text='What do you think of the book?',
        required=True,
        widget=forms.Textarea(attrs={
            "cols": 10,
            "rows": 5,
            'class': 'fw-medium p-3 form-control'
        })
    )
