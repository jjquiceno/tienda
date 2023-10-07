from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('menu', views.menu),
    path('shp', views.shp),
    path('emp2', views.emp2),
    path('edit2/<int:id>', views.edit2), 
    path('update2/<int:id>', views.update2),
    path('delete2/<int:id>', views.destroy2),
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
    path('delete/<int:id>', views.destroy),  
]  