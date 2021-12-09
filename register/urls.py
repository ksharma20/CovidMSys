from django.urls import path
from register import views

urlpatterns = [
    path('', views.dashboard, name='Dashboard'),
    path('edit/<id>/', views.edit, name='Edit'),
    path('recovered/<id>/', views.recovered, name='Recovered'),
    path('dead/<id>/', views.dead, name='Dead'),
    path('discharged/<id>/', views.discharged, name='Discharged'),
]
