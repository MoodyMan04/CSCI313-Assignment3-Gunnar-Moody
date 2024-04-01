from django.db import models
from django.urls import reverse
from django.db.models import UniqueConstraint
from django.db.models.functions import Lower
import uuid

class Genre(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, unique=True, 
                            help_text='Enter a book genre (e.g. Science Fiction, Horror, etc.)')

    def __str__(self) -> str:
        """Returns a string representation of a Genre."""
        return self.name
    
    def get_absolute_url(self):
        """Returns the url to access a specific genre instance."""
        return reverse('genre-detail', args=[str(self.id)])
    
    class Meta:
        """Class for metadata of the Genre model."""
        constraints = [UniqueConstraint(Lower('name'), name='genre_name_case_insensitive_unique', 
                                        violation_error_message='Genre already exists (case insensitive match)')]
        
class Book(models.Model):
    """Model representing a book (not a specific copy of a book)."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.RESTRICT, null=True)
    summary = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    isbn = models.CharField('ISBN', max_length=13, unique=True, 
                            help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn'
                                      '">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text='Select a genre for this book')

    def __str__(self) -> str:
        """Returns a string representation of a Book."""
        return self.title
    
    def get_absolute_url(self):
        """Returns the URL to access a detail record for this book."""
        return reverse('book-detail', args=[str(self.id)])
    
class BookInstance(models.Model):
    """Model representing a specific copy of a book."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this specific book in the library')
    book = models.ForeignKey('Book', on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On loan'),
        ('a', 'Available'),
        ('r', 'Reserved'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='m', help_text='Book availability',)

    class Meta:
        """Class for metadata of the BookInstance model."""
        ordering = ['due_back']
    
    def __str__(self) -> str:
        """Returns a string representation of a BookInstance."""
        return f'{self.id} ({self.book.title})'
    
class Author(models.Model):
    """Model representing an author."""
    """Model representing an author."""
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    class Meta:
        """Class for metadata of Author model."""
        ordering = ['last_name', 'first_name']

    def __str__(self) -> str:
        """Returns a string representation of an Author."""
        return f'{self.last_name}, {self.first_name}'
    
    def get_absolute_url(self):
        """Returns the URL to access a specific Author instance."""
        return reverse('author-detail', args=[str(self.id)])