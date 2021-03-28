from django.shortcuts import render
from django.http import HttpResponseNotFound
from django.views import View

def main_view(request):
    return render(request, 'main.html')
