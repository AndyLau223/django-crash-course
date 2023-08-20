from . import views
from django.urls import path

# urls.py connects to views for incoming requests

urlpatterns = [
    path('<slug:slug>', views.BlogView.as_view(), name='blog_view'),
    path('', views.HomeView.as_view(), name='home_view')
]
