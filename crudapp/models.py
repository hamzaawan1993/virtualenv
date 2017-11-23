# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class student(models.Model):

	name=models.CharField(max_length=100)
	department = models.CharField(max_length=150)
	University = models.CharField(max_length=200)