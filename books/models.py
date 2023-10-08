from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200)
    author = models.CharField(max_length=50)
    isbn = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=0)
    
    def __str__(self):
        return self.title
