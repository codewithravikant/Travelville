from django.contrib import admin
from pages.models import Continent, City, Country

# Register your models here.
admin.site.register(Continent)
admin.site.register(City)
admin.site.register(Country)
