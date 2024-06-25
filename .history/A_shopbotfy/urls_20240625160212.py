from django.contrib import admin
from django.urls import path, include
from django.contrib import admin
from .views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
	path('contact/', contact_page),
        path('admin/', admin.site.urls),






    path('home', include('home.urls'))
    
    
]
