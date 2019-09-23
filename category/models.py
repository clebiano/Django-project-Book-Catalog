from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=30)
    description = models.CharField(max_length=150)
    image = models.ImageField(upload_to='category', null=True, blank=True)

    def __str__(self):
        return self.category
