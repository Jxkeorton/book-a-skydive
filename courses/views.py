from django.http import HttpResponse

def courses(request):
    return HttpResponse("Courses")