# urls.py en breastcancer
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
]
