from django.urls import path
from . import views

urlpatterns = [
    path('', views.PlaneList.as_view(), name='experienced'),
    path('<slug:slug>/', views.plane_detail, name='plane_detail'),
]