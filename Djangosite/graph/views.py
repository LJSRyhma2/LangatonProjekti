from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
	return render(request, 'graph/index.html')
	
def kosteus(request):
	return render(request, 'graph/kosteus.html')
	
def kartta(request):
	return render(request, 'graph/kartta.html')
	
