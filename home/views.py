from django.shortcuts import render


# Create your views here.
def index(request):
    """ A view to render the index page """

    return render(request, 'index.html')


def about(request):
    """ A view to render the index page """

    return render(request, 'about.html')
