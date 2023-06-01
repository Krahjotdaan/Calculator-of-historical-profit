from django.db import models

class Currency(models.Model):
    name = models.CharField(max_length=100)
    literal_code = models.CharField(max_length=3)
    number_code = models.IntegerField(default=0)
    state = models.CharField(max_length=100)  

    @staticmethod
    def add(name, literal_code, number_code, state):
        Currency.objects.create(
            name=name,
            literal_code=literal_code,
            number_code=number_code,
            state=state
        )

    @staticmethod
    def get():
        return Currency.objects.all()

    @staticmethod
    def delete():
        Currency.objects.delete()


class Share(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def add(name):
        Share.objects.create(name=name)

    @staticmethod
    def get():
        return Share.objects.all()

    @staticmethod
    def delete():
        Share.objects.delete()


class PreciousMetal(models.Model):
    name = models.CharField(max_length=100)

    @staticmethod
    def add(name):
        PreciousMetal.objects.create(name=name)

    @staticmethod
    def get():
        return PreciousMetal.objects.all()

    @staticmethod
    def delete():
        PreciousMetal.objects.delete()


class CurrencyRate(models.Model):
    currency = models.ForeignKey(to=Currency, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    @staticmethod
    def add(currency, rate, profit):
        CurrencyRate.objects.create(
            currency=currency,
            rate=rate,
            profit=profit
        )

    @staticmethod
    def get():
        return CurrencyRate.objects.all()
    
    @staticmethod
    def update(rate, profit):
        CurrencyRate.rate = rate
        CurrencyRate.profit = profit

    @staticmethod
    def delete():
        CurrencyRate.objects.delete()


class ShareRate(models.Model):
    share = models.ForeignKey(to=Share, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    @staticmethod
    def add(share, rate, profit):
        ShareRate.objects.create(
            share=share,
            rate=rate,
            profit=profit
        )

    @staticmethod
    def get():
        return ShareRate.objects.all()
    
    @staticmethod
    def update(rate, profit):
        ShareRate.rate = rate
        ShareRate.profit = profit

    @staticmethod
    def delete():
        ShareRate.objects.delete()


class PreciousMetalRate(models.Model):
    metal = models.ForeignKey(to=PreciousMetal, on_delete=models.CASCADE)
    rate = models.FloatField(default=0)
    profit = models.FloatField(default=0)

    @staticmethod
    def add(metal, rate, profit):
        PreciousMetalRate.objects.create(
            metal=metal,
            rate=rate,
            profit=profit
        )

    @staticmethod
    def get():
        return PreciousMetalRate.objects.all()
    
    @staticmethod
    def update(rate, profit):
        PreciousMetalRate.rate = rate
        PreciousMetalRate.profit = profit

    @staticmethod
    def delete():
        PreciousMetalRate.objects.delete()


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
