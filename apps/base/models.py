from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=155, verbose_name = "строковое поле для имени автора.")
    birthdate = models.DateField(verbose_name = "поле даты для дня рождения автора.")
    def __str__(self) -> str:
        return self.name 
    class Meta:
        verbose_name=""
        verbose_name_plural="авторы"
class Book (models.Model):
    title = models.CharField(max_length=155, verbose_name = " строковое поле для названия книги")
    publication_year = models.DateTimeField(verbose_name = "целочисленное поле для года издания.")
    author = models.ForeignKey(Author, on_delete = models.CASCADE)
    def __str__(self) -> str:
        return self.title
    class Meta:
        verbose_name=""
        verbose_name_plural="книжки"
class Genre (models.Model):
    name = models.CharField(max_length=155, verbose_name = " строковое поле для названия жанра")
    books = models.ManyToManyField(Book, related_name='genre_book')
    def __str__(self) -> str:
        return self.name
    class Meta:
        verbose_name=""
        verbose_name_plural="жанры"




