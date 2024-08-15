from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaneList.as_view(), name='experienced'),
]