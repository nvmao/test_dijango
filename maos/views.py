from django.shortcuts import render
# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render

import django.conf as conf
from constance import config

def index(request):
    """View function for home page of site."""

    num_books = 1
    num_instances = 2
    num_instances_available = 3
    num_authors = 4

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    print(conf.settings.CONSTANCE_CONFIG['/maos'][0] )

    return render(request, 'maos/index.html', context=context)