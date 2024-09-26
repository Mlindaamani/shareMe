from django.utils.text import slugify
from django.urls import reverse
from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_birth = models.DateField()
    nationality = models.CharField(max_length=100)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse('bot:books-by-author-name', kwargs={"author": self.slug})


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return self.name

    def get_absolute_url(self):
        return reverse("bot:book-list-by-category", args=[self.slug])


class Book(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    image = models.ImageField(upload_to='books', default='book.jpg')
    slug = models.SlugField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name='books')
    authors = models.ManyToManyField(Author, related_name='books')
    isbin = models.CharField(max_length=100, null=True, blank=True)
    available = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("bot:book-detail", args=[self.id])
