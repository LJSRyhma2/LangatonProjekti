from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from graph.models import Mittaukset


def index(request):
	return render(request, 'graph/index.html')
	
def kosteus(request):
	mittauslist = Mittaukset.objects
	context = {'mittauslist': mittauslist}
	return render(request, 'graph/kosteus.html', context)
	
def kartta(request):
	return render(request, 'graph/kartta.html')
	
