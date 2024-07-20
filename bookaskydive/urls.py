from django.contrib import admin
from django.urls import path
from courses import views as courses_views
from tandems import views as tandems_views
from experienced import views as experienced_views

urlpatterns = [
    path('tandems/', tandems_views.tandems, name='courses'),
    path('courses/', courses_views.courses, name='courses'),
    path('experienced/', experienced_views.experienced, name='experienced'),
    path('admin/', admin.site.urls),
]
