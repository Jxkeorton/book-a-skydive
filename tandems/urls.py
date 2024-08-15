from django.urls import path
from . import views

urlpatterns = [
    path('', views.tandems_list, name='tandems_list'),  # Example URL pattern
]