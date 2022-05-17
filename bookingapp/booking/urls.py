from django.contrib import admin
from django.urls import path
from . import views
from .admin import admin_site

urlpatterns = [
    path('', views.index, name="index"),
    path('test/', views.TestView.as_view()),
    path('admin/', admin_site.urls)
]