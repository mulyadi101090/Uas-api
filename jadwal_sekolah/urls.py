from django.contrib import admin
from django.urls import path, include
from jadwal.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('jadwal.urls')), 
    path('', home),
]

