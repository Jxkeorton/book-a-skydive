from django.urls import path
from . import views

urlpatterns = [
    path('', views.tandems, name='example'),  # Example URL pattern
]