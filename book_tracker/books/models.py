from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=35, verbose_name='First Name')
    last_name = models.CharField(max_length=35, verbose_name='Last Name')
    biography = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, verbose_name='Date of Birth', null=True)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'bt_author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        full_name = str(self.first_name) + ' ' + str(self.last_name)
        self.slug = slugify(full_name)
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    genre = models.CharField(max_length=35, blank=True)
    authors = models.ManyToManyField(Author)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'bt_book'

    def __str__(self):
        return f'{self.title} by {[str(author) for author in self.authors.all()]}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)