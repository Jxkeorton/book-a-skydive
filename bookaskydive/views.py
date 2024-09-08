from django.shortcuts import render


def home_views(request):
    """
    Renders the homepage.

    This view handles the rendering of the homepage using the 'index.html' template.
    """
    return render(request, 'index.html')


def contact_views(request):
    """
    Renders Contact us page
    
    This view handles the rendering of the 'contact.html' template
    """
    return render(request, 'contact.html')