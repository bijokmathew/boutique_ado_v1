from django.shortcuts import render


def index(request):
    """
        A view to return the home app index page
    """
    return render(request, "home/index.html",  {'pp': "Bijo"})
