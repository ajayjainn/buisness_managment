from django.shortcuts import render
from django.http import HttpResponse
from .models import Customer


def home(request):
    customers = Customer.objects.all()
    return render(request, 'index.html', context={'customers':customers})