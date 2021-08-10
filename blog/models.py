from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class Properties(models.Model):
    address = models.CharField(max_length=100)
    society = models.CharField(max_length=100)
    size = models.FloatField()
    cost = models.FloatField()
    moskDist = models.FloatField()
    parkDist = models.FloatField()
    hospDist = models.FloatField()
    marketDist = models.FloatField()
    transitDist = models.FloatField()
    schoolDist = models.FloatField()
    uniDist = models.FloatField()

    def __str__(self):
        return self.address + ' \n is located in: ' + self.society


class FavoriteProperties(models.Model):
    propertyID = models.ForeignKey(Properties, on_delete=models.CASCADE)
    userID = models.ForeignKey(User, on_delete=models.CASCADE)
