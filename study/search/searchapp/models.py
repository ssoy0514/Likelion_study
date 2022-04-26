from django.db import models

# Create your models here.
class Building(models.Model):
    address = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    latitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)
    longitude = models.DecimalField(max_digits=10, decimal_places=7, default=0)

    def __str__(self):
        return self.name