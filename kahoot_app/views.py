from django.shortcuts import render, get_object_or_404
from .models import *

# Import Pagination
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    categories = Category.objects.all()

    p = Paginator(Category.objects.all(), 10)
    page = request.GET.get('page')
    page_number = p.get_page(page)

    q = request.GET.get('q')
    if q:
        categories = Category.objects.filter(title__icontais=q)
    context = {
        'categories': categories,
        'page_number': page_number,
    }
    return render(request, 'kahoot/home.html', context)

def detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'kahoot/detail.html', context)