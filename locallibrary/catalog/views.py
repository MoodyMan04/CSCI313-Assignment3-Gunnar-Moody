from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre

def index(request):
    """View function for home page of site."""

    # Generate count of Books and BookInstances.
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Filter available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()

    # Generate count of Authors.
    num_authors = Author.objects.count()

    # Generate count of Genres.
    num_genres = Genre.objects.all().count()

    # Generate count of Books with word 'Road' in the title
    num_books_road = Book.objects.all().filter(title__contains='road').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_books_road': num_books_road
    }

    return render(request, 'index.html', context=context)
