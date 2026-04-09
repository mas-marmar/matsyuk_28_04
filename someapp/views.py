from django.views.generic import ListView, DetailView
from django.db.models import Count
from .models import Book

class AuthorListView(ListView):
    """Список всех авторов"""
    template_name = 'author_list.html'
    context_object_name = 'authors'

    def get_queryset(self):
        authors = Book.objects.values('author').annotate(
            book_count=Count('id')
        ).order_by('author')
        return authors

class BookListView(ListView):
    """Список книг конкретного автора"""
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

    def get_queryset(self):
        author_name = self.kwargs.get('author')
        return Book.objects.filter(author=author_name)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['author_name'] = self.kwargs.get('author')
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'
    context_object_name = 'book'