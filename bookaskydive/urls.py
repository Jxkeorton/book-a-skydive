from django.contrib import admin
from django.urls import path
from courses import views as courses_views
from tandems import views as tandems_views

urlpatterns = [
    path('tandems/', tandems_views.tandems, name='courses'),
    path('courses/', courses_views.courses, name='courses'),
    path('admin/', admin.site.urls),
]
