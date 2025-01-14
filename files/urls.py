from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('file/<uuid:unique_id>/', views.file_share, name='file_share'),
]
