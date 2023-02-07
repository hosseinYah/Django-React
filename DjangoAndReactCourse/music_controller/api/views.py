from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('Hello world!')

def homepage(request):
    return HttpResponse('Home Page! - <a href=\'http://127.0.0.1:8000/api/main\'>Main Page<a>')