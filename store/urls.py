from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('services', views.Services, name= 'services' ),
    path('about', views.About, name= 'about' ),
    path('contact', views.addContact, name= 'contact' ),
    path('blog/', views.Blog, name= 'blog' ),
   
  
]
