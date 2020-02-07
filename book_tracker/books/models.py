from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    first_name = models.CharField(max_length=35, verbose_name='First Name')
    last_name = models.CharField(max_length=35, verbose_name='Last Name')
    biography = models.TextField(blank=True)
    date_of_birth = models.DateField(blank=True, verbose_name='Date of Birth', null=True)
    slug = models.SlugField(unique=True)
    full_name = models.CharField(max_length=70)

    class Meta:
        db_table = 'bt_author'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        full_name = str(self.first_name) + ' ' + str(self.last_name)
        self.slug = slugify(full_name)
        self.full_name = self.get_full_name()
        super(Author, self).save(*args, **kwargs)


class Book(models.Model):
    GENRE_CHOICES = [
        ('NF', 'Non-Fiction'),
        ('PT', 'Poetry'),
        ('NV', 'Novel'),
        ('AN', 'Anthology'),
        ('PL', 'Play')
    ]

    title = models.CharField(max_length=55)
    description = models.TextField(blank=True)
    pages = models.IntegerField()
    genre = models.CharField(max_length=2, choices=GENRE_CHOICES)
    authors = models.ManyToManyField(Author)
    slug = models.SlugField(unique=True)

    class Meta:
        db_table = 'bt_book'

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Book, self).save(*args, **kwargs)

    def get_average_rating(self):
        if self.review_set.all():
            ratings = [int(review.rating) for review in self.review_set.all()]
            return round(sum(ratings)/len(ratings),1)
        return 0

    def get_review_count(self):
        if self.review_set.all():
            reviews = [review for review in self.review_set.all()]
            return len(reviews)
        return 0
