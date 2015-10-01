from django.db import models

# Create your models here.
class Newsletter(models.Model):
    email = models.EmailField()
    full_name = models.CharField(120)
    timestamp = models.DateTimeField()