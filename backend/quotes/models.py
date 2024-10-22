from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    

class Quote(models.Model):
    text  = models.TextField()
    author = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='quotes')

    def __str__(self):
        return f'"{self.text}" - {self.author}'
