from django.db import models

# Create your models here.
class Family(models.Model):
    family = models.CharField(max_length=50, null=False)
