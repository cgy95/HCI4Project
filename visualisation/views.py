from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'visualisation/index.html', context_dict)
