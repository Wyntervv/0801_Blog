from django.db import models
class Board(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.IntegerField()

# Create your models here.
