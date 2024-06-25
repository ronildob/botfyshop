from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls'))
    path('products/', ProductListView.as_view()),
    path('products-fbv/', product_list_view),
    
]
