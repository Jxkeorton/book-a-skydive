from django.contrib import admin
from django.urls import path, include
from .views import home_views, contact_views

urlpatterns = [
    path('', home_views, name='home'),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path('contact-us/', contact_views, name='contact'),
    path('course/', include('courses.urls'), name='courses_urls'),
    path('sport/', include('experienced.urls'), name="experienced_urls"),
    path('tandems/', include('tandems.urls'), name='tandems_urls'),
    path('profile/', include('userprofile.urls'), name='userprofile'),
]
