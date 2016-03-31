from django.contrib import admin
import models

# Register your models here.
admin.site.register(models.Company)
admin.site.register(models.Platform)
admin.site.register(models.Genre)
admin.site.register(models.Review)
admin.site.register(models.Game)
admin.site.register(models.CompanyGame)
admin.site.register(models.PlatformGame)
admin.site.register(models.GenreGame)
admin.site.register(models.GameReview)
