from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(requeest):
    return HttpResponse('<i><h1>This my first app</h1>')

def second(requeest):
    return HttpResponse('<i><h1>this is Harshad sir class..<h1/>')
