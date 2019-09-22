from django.db import models
from author.models import Author
from category.models import Category
from comment.models import Comment
from review.models import Review


class Book(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    author = models.ManyToManyField(Author)
    category = models.ManyToManyField(Category)
    comment = models.ManyToManyField(Comment)
    review = models.ManyToManyField(Review)
    image = models.ImageField(upload_to='book', null=True, blank=True)

    def __str__(self):
        return self.title
