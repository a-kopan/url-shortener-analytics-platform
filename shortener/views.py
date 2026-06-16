from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def generate_link(request):
    return HttpResponse("Generate link placeholder")

def redirect(request):
    return HttpResponse("Redirect placeholder")

