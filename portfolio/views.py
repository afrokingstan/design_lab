from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Portfolio
from .forms import PortfolioForm


def all_portfolio(request):
    """ A view to show all portfolio """

    portfolios = Portfolio.objects.all()

    context = {
        'portfolios': portfolios,
    }

    return render(request, 'portfolio/all_portfolio.html', context)


def portfolio_detail(request, portfolio_id):
    """ A view to show individual portfolio details """

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)

    context = {
        'portfolio': portfolio,
    }

    return render(request, 'portfolio/portfolio_detail.html', context)



@login_required
def add_portfolio(request):
    """ Add a portfolio to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

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


@login_required
def edit_portfolio(request, portfolio_id):
    """ Edit a portfolio in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    if request.method == 'POST':
        form = PortfolioForm(request.POST, request.FILES, instance=portfolio)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated to Portfolio!')
            return redirect(reverse('portfolio_detail', args=[portfolio.id]))
        else:
            messages.error(request, 'Failed to update to Portfolio. Please ensure the form is valid.')
    else:
        form = PortfolioForm(instance=portfolio)
        messages.info(request, f'You are editing {portfolio.name}')

    template = 'portfolio/edit_portfolio.html'
    context = {
        'form': form,
        'portfolio': portfolio,
    }

    return render(request, template, context)


@login_required
def delete_portfolio(request, portfolio_id):
    """ Delete a portfolio from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    portfolio = get_object_or_404(Portfolio, pk=portfolio_id)
    portfolio.delete()
    messages.success(request, 'Portfolio deleted!')
    return redirect(reverse('portfolio'))

