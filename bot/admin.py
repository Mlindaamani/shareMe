from django.contrib import admin
from .models import Book, Category, Author


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'date_birth', 'nationality', 'slug']
    list_filter = ['nationality']
    prepopulated_fields = {'slug': ['name']}


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'slug', 'available', 'book_status']
    list_filter = ['authors', 'category']
    prepopulated_fields = {'slug': ['name']}
    list_editable = ['price']
    list_per_page = 12

    @admin.display(ordering='price')
    def book_status(self, book: Book):
        if book.price < 400.0:
            return 'Cheap'
        else:
            return "Expensive"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name']
    prepopulated_fields = {'slug': ['name']}
