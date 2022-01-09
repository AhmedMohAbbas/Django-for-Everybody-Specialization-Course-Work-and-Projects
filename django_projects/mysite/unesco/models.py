from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=128)
    year = models.IntegerField(null=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    region = models.ForeignKey('Region', on_delete= models.CASCADE)
    state = models.ForeignKey('States', on_delete= models.CASCADE)
    iso = models.ForeignKey('Iso', on_delete= models.CASCADE)
    description = models.TextField(max_length=512)
    justification = models.TextField(max_length=512)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area_hectares = models.FloatField(null=True)



    def __str__(self) :
        return self.name



class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name



class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class States(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Iso(models.Model):
    name = models.CharField(max_length=8)

    def __str__(self):
        return self.name
