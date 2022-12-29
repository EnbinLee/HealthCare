from django.urls import path, include
from HealthCare import views

urlpatterns = [
    path('', views.HomePage, name='home'),
]
