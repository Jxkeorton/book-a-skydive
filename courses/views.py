from django.shortcuts import render

def courses_list(request):
    """
    Renders the Tandem page
    """

    return render(
        request,
        template_name = "courses/courses.html",
    )