from django.db import models

class Currency(models.Model):
    state = models.CharField(max_length=100)
    code = models.CharField(max_length=3)
    exchange_rate = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    def add(state, code, exchange_rate, profit):
        Currency.objects.create(
            state=state,
            code=code,
            exchange_rate=exchange_rate,
            profit=profit
        )

    def get():
        return Currency.objects.all()
    
    def update(exchange_rate, profit):
        exchange_rate=exchange_rate
        profit=profit

    def delete():
        Currency.objects.delete()


class Share(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    def add(name, cost, profit):
        Share.objects.create(
            name=name,
            cost=cost,
            profit=profit
        )

    def get():
        return Share.objects.all()
    
    def update(cost, profit):
        cost=cost
        profit=profit

    def delete():
        Share.objects.delete()


class PreciousMetal(models.Model):
    name = models.CharField(max_length=100)
    cost = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    def add(name, cost, profit):
        PreciousMetal.objects.create(
            name=name,
            cost=cost,
            profit=profit
        )

    def get():
        return PreciousMetal.objects.all()
    
    def update(cost, profit):
        cost=cost
        profit=profit

    def delete():
        PreciousMetal.objects.delete()


class SharesBriefcase(models.Model):
    shares = models.ManyToManyField(to=Share)
    cost = models.FloatField(default=0)
    reference_point = models.DateField(default=0)
    profit = models.FloatField(default=0)

    def add(shares, cost, reference_point, profit):
        SharesBriefcase.objects.create(
            shares=shares,
            cost=cost,
            reference_point=reference_point,
            profit=profit
        )

    def get():
        return SharesBriefcase.objects.all()
    
    def update():
        pass

    def delete():
        SharesBriefcase.objects.delete()
