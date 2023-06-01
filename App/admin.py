from django.contrib import admin
import App.models as models

admin.site.register(models.Currency)
admin.site.register(models.Share)
admin.site.register(models.PreciousMetal)
admin.site.register(models.CurrencyRate)
admin.site.register(models.ShareRate)
admin.site.register(models.PreciousMetalRate)
admin.site.register(models.SharesBriefcase)
