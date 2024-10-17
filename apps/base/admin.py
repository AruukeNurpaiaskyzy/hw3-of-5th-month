from django.contrib import admin
from .models import Author, Book, Genre


# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_play = ('name', 'birthdate') 
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_play = ('title', 'publication_year', 'author') 
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_play = ('name', 'books') 

