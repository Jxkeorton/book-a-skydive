from django.http import HttpResponse

# Create your views here.
def user_profile_view(request):
    return HttpResponse("User Profile")
