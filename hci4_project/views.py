from django.shortcuts import render
from django.contrib.auth import authenticate, login

def index(request):
    if request.user.is_authenticated():
	return render(request, 'visualisation/index.html')
    else:
	return render(request, 'index.html')

