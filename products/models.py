from django.db import models

# Create your models here.
class ProductModel(models.Model):
    name = models.CharField(max_length=120, null=False, blank=False)
    price = models.FloatField(null=False, blank=False)
    creator = models.CharField(max_length=120, null=True, blank=False)
