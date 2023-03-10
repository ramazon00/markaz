from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('users/', views.user, name='user'),
    path('add/', views.AddView.as_view(), name='add'),
    path('edit/', views.EditView.as_view(), name='edit'),
    path('delete/', views.Delete.as_view(), name='delete'),
]