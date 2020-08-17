from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import Products
from .forms import ProductsForm


def index(request):
    products = Products.objects.all()
    return render(request, 'crud/index.html', {"products": products})


def add(request):
    error = ''
    if request.method == 'POST':
        form = ProductsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма была неверной'

    form = ProductsForm()
    context = {
        'form': form
    }
    return render(request, 'crud/add.html', context)

