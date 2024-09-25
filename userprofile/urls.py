from django.urls import path
from .views import user_profile_view 

app_name = 'userprofile'

urlpatterns = [
    path('userprofile/', user_profile_view, name='user_profile'), 
]
