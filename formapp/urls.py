from django.urls import path
from . import views

urlpatterns = [
    path('', views.submit_info, name='submit'),
    path('success/', views.success, name='success'),
]