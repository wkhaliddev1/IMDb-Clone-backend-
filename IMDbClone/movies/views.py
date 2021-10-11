from django.shortcuts import render

# React index.html view

def index(request):
    return render(request, 'index.html')
