from django.urls import path
from . import views

urlpatterns = [
    path('plane-book/', views.PlaneList.as_view(), name='experienced'),
]