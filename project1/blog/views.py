from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return HttpResponse("Blog Home page")


def about(request):
  return HttpResponse("Blog About page")
