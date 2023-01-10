from django.shortcuts import render
from django.http import HttpResponse

def landing_view(request):
    context = {'name':'Automax'}
    return render(request, 'main/main.html', context)
