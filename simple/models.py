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
    height = models.IntegerField()
    weight = models.IntegerField()
    gender = models.CharField(max_length=1 , choices=gender_choices,)

class mettable(models.Model):
    activity_choices = (
            ('0.95' , "Sleeping"),
            ('1.0', 'watching_tv'),
            ('1.3', 'writing_or_typing'),
            ('2.0', 'walking'),
        )
    level_choices = (
            ('l' , "Light"),
            ('m', 'Moderate'),
            ('v', "Vigorous"),
        )
    activity = models.CharField(max_length=10 , choices=activity_choices,)
    level = models.CharField(max_length=1 , choices=level_choices,)
    hours = models.IntegerField()
    minutes = models.IntegerField()
