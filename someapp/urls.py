from django.urls import path
from .views import AuthorListView, BookListView, BookDetailView

urlpatterns = [
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('authors/<str:author>/books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
]