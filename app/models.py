from django.db import models
from django.core.validators import RegexValidator


class Author(models.Model):
    author_profile = models.ImageField(upload_to="media/author")
    name = models.CharField(max_length=100, null=True)
    about_author = models.TextField()

    def __str__(self):
        return self.name



