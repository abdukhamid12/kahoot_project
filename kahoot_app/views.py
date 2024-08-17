from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Import Pagination
from django.core.paginator import Paginator
# Create your views here.

def home(request):
    categories = Category.objects.all()
    search = request.GET.get('search')

    if search:
        categories = categories.filter(title__icontains=search)

    p = Paginator(categories, 5)
    page = request.GET.get('page')
    page_number = p.get_page(page)

    context = {
        'categories': page_number,
        'search': search,
        'page_number': page_number,
    }
    return render(request, 'kahoot/home.html', context)

def detail_view(request, pk):
    category = get_object_or_404(Category, pk=pk)
    context = {
        'category': category,
    }
    return render(request, 'kahoot/detail.html', context)

def list_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    category_form = CategoryForm()

    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    question_form = QuestionForm()

    context = {
        'category_form': category_form,
        'question_form': question_form,
    }
    return render(request, 'kahoot/category_style.html', context)