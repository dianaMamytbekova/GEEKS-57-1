from django.contrib import admin
from . import models

admin.site.register(models.Films)
admin.site.register(models.Reviews)
admin.site.register(models.Car)
admin.site.register(models.Person)


