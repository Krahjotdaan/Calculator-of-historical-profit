from django.db import models

class Currency(models.Model):
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    exchange_rate = models.FloatField(default=0)
    profit = models.FloatField(default=0)


class Share(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    profit = models.FloatField(default=0)


class PreciousMetal(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    profit = models.FloatField(default=0)


class SharesBriefcase(models.Model):
    shares = models.ManyToManyField(to=Share)
    cost = models.FloatField(default=0)
    profit = models.FloatField(default=0)
