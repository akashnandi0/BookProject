from django.db import models

class Author(models.Model):
    author_name = models.CharField(max_length=50,null=True)

    def __str__(self):
        return self.author_name

class Book(models.Model):
    title = models.CharField(max_length=50,null=True)
    author_name = models.ManyToManyField(Author)
    publication_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title
