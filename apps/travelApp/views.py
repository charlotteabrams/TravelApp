from django.shortcuts import render

# Create your views here.

def index(request):

	return render(request, 'travelAppTemplates/index.html')

def register(request):

	return render(request, 'travelAppTemplates/registration.html')

def process(request):

	pass

def login(request):

	pass
 