from django.db import models

# Create your models here.
class students(models.Model):
    name=models.CharField(max_length=100)
    email = models.CharField(unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name
