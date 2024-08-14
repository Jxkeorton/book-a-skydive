from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tandems.urls'), name='tandems_urls'),
    path('course/', include('courses.urls'), name='courses_urls'),
    path('user/', include('experienced.urls'), name="experienced_urls"),
    path('admin/', admin.site.urls),
    path("accounts/", include("allauth.urls")),
]
