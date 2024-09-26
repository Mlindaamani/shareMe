
from . import views
from django.urls import path

app_name = 'bot'

urlpatterns = [

    path(
        '',
        views.book_list,
        name='book-list'
    ),

    path(
        'category/<slug:category_slug>/',
        views.book_list,
        name='book-list-by-category'
    ),

    path(
        'author/<slug:author>/',
        views.book_list,
        name='books-by-author-name'),

    path(
        'book/<int:id>/view-book-detail/',
        views.book_detail,
        name='book-detail'),

    path(
        'share/<int:id>/share-book/',
        views.share_book,
        name='share-book'
    ),

    path(
        'dashboard/',
        views.dashboard,
        name='dashboard'
    ),
]
