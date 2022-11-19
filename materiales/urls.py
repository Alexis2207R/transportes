from django.urls import path
from . import views

urlpatterns = [
    path('materiales/', views.about, name='material')
]
