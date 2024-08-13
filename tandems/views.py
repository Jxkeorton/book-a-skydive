from django.http import HttpResponse
from django.shortcuts import render

def tandems(request):
    """
    Renders the Tandem page
    """

    return render(
        request,
        "tandems/tandem.html",
    )