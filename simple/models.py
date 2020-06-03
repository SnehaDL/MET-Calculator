# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class bmrtable(models.Model):
    gender_choices = (
            ('m' , "Male"),
            ('f', 'Female')
	)
    age    = models.IntegerField()
    height = models.DecimalField(max_digits=4, decimal_places=2)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    gender = models.CharField(max_length=1 , choices=gender_choices,)

class mettable(models.Model):
    activity_choices = (
            ('7.5' , "cycling"),
            ('14', 'cycling up hill'),
            ('6', 'jogging'),
            ('6', 'running'),
            ('8', 'housework'),
            ('4', 'skipping'),
            ('11', 'walkingstairs'),
            ('5', 'pilates'),
            ('3', 'weight'),
        )
    level_choices = (
            ('1' , "Light"),
            ('2', 'Moderate'),
            ('3', "Vigorous"),
        )
    activity = models.CharField(max_length=10 , choices=activity_choices,)
    level = models.CharField(max_length=1 , choices=level_choices,)
    hours = models.IntegerField()
    minutes = models.IntegerField()
