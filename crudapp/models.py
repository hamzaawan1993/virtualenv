# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Employee(models.Model):

	
	employee_name=models.CharField(max_length=100)
	employee_gender =models.CharField(max_length=20)
	
	def __str__(self):
		return self.employee_name

    
class Department(models.Model):
	department_name=models.CharField(max_length=100)
	
	def __str__(self):
		return self.department_name