from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages

from django.db.models import Q
from django.db.models.functions import Lower

from .models import Portfolio
from .forms import PortfolioForm


def all_portfolio(request):
    """ A view to show all products, including sorting and search queries """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'portfolio/all_portfolio.html', context)



def add_portfolio(request):
    """ Add a product to the store """
    form = PortfolioForm()
    template = 'portfolio/add_portfolio.html'
    context = {
        'form': form,
    }

    return render(request, template, context)