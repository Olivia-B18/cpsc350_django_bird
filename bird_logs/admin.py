from django.contrib import admin

from .models import Bird, Sighting

admin.site.register(Bird)
admin.site.register(Sighting)
