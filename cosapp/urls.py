from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('segundo/',views.segundo, name='segundo'),
    path('carta/', views.carta, name='carta'),
]