from django.db import models


# Create your models here.
class Continent(models.Model):
    name = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(unique=True, max_length=50)
    continent = models.ForeignKey(to=Continent, on_delete=models.CASCADE, related_name='countries')

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(unique=True, max_length=50)
    description = models.CharField(unique=False, max_length=500)
    country = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name='cities')

    def __str__(self):
        return self.name
