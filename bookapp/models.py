from django.db import models

# Create your models here.

class Book(models.Model):
    book_name=models.CharField(max_length=150,unique=True)
    author=models.CharField(max_length=150)
    price=models.IntegerField()
    pages=models.IntegerField()


def __str__(self):
    return self.book_name