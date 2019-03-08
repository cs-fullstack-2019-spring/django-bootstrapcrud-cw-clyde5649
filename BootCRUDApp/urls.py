from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name=''),
    path('garage/',views.garage,name='garage'),
    path('edit/',views.edit,name='edit'),
]