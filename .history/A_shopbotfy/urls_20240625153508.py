from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from django.urls import path
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
    
    
]
