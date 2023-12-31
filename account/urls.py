from django.urls import path, include
from .import views

app_name = "account"

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('settings/', views.settings, name='settings'),
    path('delete_account/', views.delete_account, name='delete_account'),
]