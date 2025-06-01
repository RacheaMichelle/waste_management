from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_waste, name='waste_list'),
    path('update/<int:pk>/', views.update_waste, name='waste_update'),
    path('delete/<int:pk>/', views.delete_waste, name='waste_delete'),
]