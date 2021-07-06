from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('usStates', views.usStates, name='usStates'),
    path('refresh', views.refresh, name='refresh'),
    path('refreshData', views.refreshData, name='refreshData'),
    path('refreshReport', views.refreshReport, name='refreshReport'),
]