from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from .models import Author, Book, Genre
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer


# Create your views here.
class AuthorAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):

 queryset = Author.objects.all()
 serializer_class = AuthorSerializer 
class BookAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):

 queryset = Book.objects.all()
 serializer_class = BookSerializer 
class GenreAPI(GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                ):

 queryset = Genre.objects.all()
 serializer_class = GenreSerializer 
