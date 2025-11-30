from django.db import models

# Create your models here.
from django.db import models

class FuelStation(models.Model):
    opis_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=10)
    retail_price = models.FloatField()

    class Meta:
        indexes = [
            models.Index(fields=['retail_price']),
        ]

    def __str__(self):
        return f"{self.name} ({self.city}, {self.state})"
