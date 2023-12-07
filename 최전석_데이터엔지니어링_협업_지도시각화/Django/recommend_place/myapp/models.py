from django.db import models

# Create your models here.
class Place(models.Model):
    city = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    age = models.CharField(max_length=200)
    companion = models.CharField(max_length=200)
    rating = models.FloatField()

    def __str__(self):
        return f"{self.city}, {self.gender}, {self.age}, {self.companion}, {self.rating}"

