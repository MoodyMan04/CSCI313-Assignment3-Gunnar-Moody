from django.contrib import admin
from .models import Author, Genre, Book, BookInstance, Language

admin.site.register(Genre)
admin.site.register(Language)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Define admin class for Author."""
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Define admin class for Book."""
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    """Define admin class for BookInstance."""
    list_display = ('book', 'status', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = ((None, {'fields': ('book', 'imprint', 'id')}),
                ('Availability', {'fields': ('status', 'due_back')}),)
    

