from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.category
