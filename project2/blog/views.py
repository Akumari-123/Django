from django.shortcuts import render
from django.http import HttpResponse
def post_details(request,post_id):
  return HttpResponse(f"<h1>Show blog post {post_id}</h1>")
# Create your views here.
def user_profile(request,username):
  return HttpResponse(f"<h1>Profile of user:{username}</h1>")
def article_by_year(request,year):
  return HttpResponse(f"<h1>articles from the year:{year}</h1>")
def article_details(request,**kwargs):
  return HttpResponse(f"<h1>Data: {kwargs}</h1>")