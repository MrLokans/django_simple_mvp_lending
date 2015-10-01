from django.db import models

# Create your models here.
# https://docs.djangoproject.com/en/1.8/ref/models/fields/


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, default='John Doe', blank=True, null=True)
    # auto add timestamp on create
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # represented in admin site
    def __unicode__(self): # __str__  for python 3
        return self.email