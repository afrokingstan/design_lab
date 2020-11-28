from django.shortcuts import render, redirect, reverse, get_object_or_404

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