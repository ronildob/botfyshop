from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from .views import home_page, about_page, contact_page, login_page, register_page
from products.views import ProductListView, product_list_view, ProductDetailView, product_detail_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page),
    path('about/', about_page),
	path('contact/', contact_page),
    path('login/', login_page),
    path('register/', register_page),
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view), 
    path('products/<int:pk>', ProductDetailView.as_view()),
    path('products-fbv/<int:pk>', product_detail_view), 







    path('home', include('home.urls'))
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
