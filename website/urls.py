from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('services', views.services, name='services'),
    path('graphics/', views.graphics, name='graphics'),
    path('commercial_adverts/', views.commercial_adverts, name='commercial_adverts'),
    path('documentaries/', views.documentaries, name='documentaries'),
    path('photography/', views.photography, name='photography'),
    path('internet_solutions/', views.internet_solutions, name='internet_solutions'),
    path('data_processing/', views.data_processing, name='data_processing'),
]
