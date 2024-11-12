# urls.py en breastcancer
from django.urls import path
from . import views

urlpatterns = [
    path('diagnosis/', views.diagnosis_view, name='diagnosis'),
]
