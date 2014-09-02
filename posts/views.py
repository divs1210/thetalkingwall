from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the post index.")

def apost(request, post_id):
    return HttpResponse("You're looking at post %s." % post_id)
