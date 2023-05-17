from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('view/<uuid:pk>/', views.details, name='view'),
    path('edit/<uuid:pk>/', views.edit, name='edit'),
    path('delete/<uuid:pk>/', views.remove, name='delete'),
]