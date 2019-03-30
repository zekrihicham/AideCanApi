from django.db import models

# Create your models here.
class Case(models.Model):
    radius_mean = models.FloatField()
    texture_mean = models.FloatField()
    perimeter_mean = models.FloatField()
    area_mean = models.FloatField()
    smoothness_mean = models.FloatField()
    compactness_mean = models.FloatField()
    concavity_mean = models.FloatField()
    concave_points_mean = models.FloatField()
    symmetry_mean = models.FloatField()
    fractal_dimension_mean = models.FloatField()
    diagnostic=models.IntegerField(blank=True,null=True)



