from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def baby(requeest):
    return HttpResponse('<i><h1>In Baby movie super...</h1>')

def hai(requeest):
    return HttpResponse('<i><h1>hai ra bangarammm..<h1>')