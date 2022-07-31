from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, "home.html")

    # HttpResponse("Hello, world. This is a django boilerplate!")