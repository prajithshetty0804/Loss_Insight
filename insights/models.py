class WeeklyLossRecord(models.Model):
    plant_name = models.CharField(max_length=100)
    week_number = models.IntegerField()
    loss_value = models.FloatField()
