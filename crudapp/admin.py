# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Employee
from .models import Department

class EmployeeAdmin(admin.ModelAdmin):
	list_display = ["id","employee_name","employee_gender"]
	class Meta:
		model = Employee

class DepartmentAdmin(admin.ModelAdmin):
	list_display = ["id","department_name"]
	class Meta:
		model = Department

admin.site.register(Employee,EmployeeAdmin)
admin.site.register(Department,DepartmentAdmin)
