from django.urls import path
from . import views

urlpatterns = [
    path('example/', views.courses, name='example'),  # Example URL pattern
]