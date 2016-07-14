from __future__ import unicode_literals

from django.db import models


# Create your models here.

class Case(models.Model):
    seeker_email = models.CharField(max_length=64)
    entity = models.CharField(max_length=128)
    address1 = models.CharField(max_length=128, blank=True)
    address2 = models.CharField(max_length=128, blank=True)
    city = models.CharField(max_length=64, blank=True)
    zip = models.CharField(max_length=10, blank=True)
    state = models.CharField(max_length=64, blank=True)
    country = models.CharField(max_length=64, blank=True)
    website = models.CharField(max_length=128)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __unicode__(self):
        return self.entity

    def __str__(self):
        return self.entity
