from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView

from core.erp.models import Category
from core.erp.forms import CategoryForm


def category_list(request):
    data = {
        'title': 'Listado de Categorías',
        'categories': Category.objects.all(),
    }
    return render(request, 'category/list.html', data)


class CategoryListView(ListView):
    model = Category
    template_name = "category/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Categorías'
        return context



class CategoryCreateView(CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'category/create.html'
    success_url = reverse_lazy('erp:category_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de una  Categoría'
        return context