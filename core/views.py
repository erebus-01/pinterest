from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return render(request, 'home.html')


def signup(request):
  return render(request, 'pinterest.html')