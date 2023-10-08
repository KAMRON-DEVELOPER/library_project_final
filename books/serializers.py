from rest_framework import serializers
from .models import Book
from rest_framework.exceptions import ValidationError


class BookSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        fields = ('id', 'title', 'subtitle', 'author', 'isbn', 'price',)

    def validate(self, data):
        author = data.get('author', None)
        title = data.get('title', None)
        if not title.isalpha():
            raise ValidationError({"status" : False, "message" : "kitob nomi harflardan iborat bo'lishi kerak."})
        
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError({"status" : False, "message" : "kitob nomi bilan author nomi unique bo'lishi kerak."})
        
        return data


