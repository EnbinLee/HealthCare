from django.urls import path
from HealthCare import views

urlpatterns = [
    path('', views.HomePage, name='home'),
]
