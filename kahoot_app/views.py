from django.shortcuts import render, get_object_or_404
from .models import *
# Create your views here.

def home(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'kahoot/home.html', context)

def detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'kahoot/detail.html', context)