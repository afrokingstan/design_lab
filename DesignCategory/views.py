from django.shortcuts import render

# Create your views here.


def design_category(request):
    """ A view to return the index page """

    return render(request, 'DesignCategory/design_category.html')
