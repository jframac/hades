from django.shortcuts import render

from core.erp.models import Category

def myfirstview(request):
    data = {
        'name': 'Francisco',
        'categories': Category.objects.all()
    }

    return render(request, 'index.html', data)
