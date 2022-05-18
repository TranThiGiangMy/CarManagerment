from django.contrib import admin
from django.urls import path, include
from . import views
from .admin import admin_site
from rest_framework import routers
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('routes', views.RoutesViewSet)
router.register('train', views.TrainViewSet)
router.register('ticket', views.TicketViewSet)


urlpatterns = [
    path('', include(router.urls)),
    # path('', views.index, name="index"),
    # path('test/', views.TestView.as_view()),
    path('admin/', admin_site.urls)]