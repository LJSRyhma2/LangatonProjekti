from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the graph index.")
	
def kosteus(request):
	return HttpResponse("Kosteusnäkymä")
	
def kartta(request):
	return HttpResponse("Karttanäkymä")
	
