from django.db import models

class PlantLoss(models.Model):
    plant = models.CharField(max_length=100)
    week = models.IntegerField()
    loss = models.FloatField()

    def __str__(self):
        return f"{self.plant} - Week {self.week}"
