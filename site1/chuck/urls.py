from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('api/joke/', views.get_joke),
     path('api/news/', views.get_news),
    path('api/translate/', views.translate),
    path('api/translate2/', views.translate2), 
    path('api/translate3/', views.translate3),        
]
