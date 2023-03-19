from django.db import models


class Region(models.Model):
    """
    Region object
    """

    codigo = models.CharField(max_length=10, primary_key=True)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    """
    Provincia object
    """

    codigo = models.CharField(max_length=10, primary_key=True)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Comuna(models.Model):
    """
    Comuna object
    """

    codigo = models.CharField(max_length=10, primary_key=True)
    tipo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=255)
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)
    url = models.URLField(max_length=200)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    provincia = models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
