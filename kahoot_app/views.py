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

def create_page_category(request):
    if request.method == 'POST':
        form = CreateCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    form = CreateCategoryForm()

    return render(request, 'kahoot/create_page.html', {"form": form, 'categories': Category.objects.all()})

def category_style(request):
    return render(request, 'kahoot/category_style.html')


def create_question(request):
    if request.method == 'POST':
        form = CreateQuestionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
    form = CreateQuestionForm()
    return render(request, 'kahoot/quiz_page.html', {"form": form, 'categories': Question.objects.all()})
