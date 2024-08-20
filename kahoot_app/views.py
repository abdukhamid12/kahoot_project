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
        'search': search if search else '',
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
    category_form = CategoryForm()
    question_form = QuestionForm()
    option_form = OptionForm()
    option_formset = OptionFormSet()

    context = {
        'category_form': category_form,
        'question_form': question_form,
        'option_form': option_form,
        'option_formset': option_formset
    }
    return render(request, 'kahoot/category_style.html', context)


def category_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home-view')
        else:
            print(form.errors)
    category_form = CategoryForm()
    question_form = QuestionForm()
    option_form = OptionForm()
    option_formset = OptionFormSet()

    context = {
        'category_form': category_form,
        'question_form': question_form,
        'option_form': option_form,
        'option_formset': option_formset
    }
    return render(request, 'kahoot/create_page.html', context)


def create_question(request):
    if request.method == 'POST':
        question_form = QuestionForm(request.POST, request.FILES)
        option_formset = OptionFormSet(request.POST, instance=question_form.instance)
        if question_form.is_valid() and option_formset.is_valid():
            question = question_form.save()
            option_formset.save()
            return redirect('home-view')  # Replace with your success URL
    else:
        question_form = QuestionForm()
        option_formset = OptionFormSet()

    return render(request, 'kahoot/create_page.html', {
        'question_form': question_form,
        'option_formset': option_formset,
    })