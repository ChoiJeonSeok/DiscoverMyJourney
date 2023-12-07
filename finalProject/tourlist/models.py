from django.db import models
from django.conf import settings

class Tourmodel(models.Model):
    location = models.CharField(max_length=200)
    location_code = models.CharField(max_length=5)
    positive = models.TextField()
    negative = models.TextField()
    image = models.ImageField()
    tour_loc_1 = models.TextField()
    tour_loc_2 = models.TextField()
    tour_loc_3 = models.TextField()
    def __str__(self):                 
        return f"{self.location}, {self.location_code}, {self.positive}, {self.negative}, {self.tour_loc_1},{self.tour_loc_2},{self.tour_loc_3}"
