from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Portfolio
from .forms import PortfolioForm


def all_portfolio(request):
    """ A view to show all portfolio """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'portfolio/all_portfolio.html', context)


def add_portfolio(request):
    """ Add a portfolio to the store """
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added to Portfolio!')
            return redirect(reverse('add_portfolio'))
        else:
            messages.error(request, 'Failed to add to Portfolio. Please ensure the form is valid.')
    else:
        form = PortfolioForm()
    template = 'portfolio/add_portfolio.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


def portfolio_detail(request, portfolio_id):
    """ A view to show individual product details """

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio_detail.html', context)