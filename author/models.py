from django.db import models


class Author(models.Model):
    author = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.author
