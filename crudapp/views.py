# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse
#from django.views.decorators.csrf import csrf_exempt
from django.template import loader

import datetime
# Create your views here.
#@csrf_exempt

def index(request):
	return HttpResponse("<h1> Crud project on virtual environment </h1")

def hello(request):
	today = datetime.datetime.now().date()
	if request.method == 'POST':
		name = request.POST.get('name')
		gender = request.POST.get('gender')

		template = loader.get_template('show_data.html')
		return HttpResponse(template.render(context,request,{"today" : today}))
	
	else:

		template = loader.get_template('hello.html')
		return render(request, "hello.html", {"today" : today})

