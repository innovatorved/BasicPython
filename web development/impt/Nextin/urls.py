from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('<int:id>/',views.detail, name= 'Detail'),
    path('',views.Course ,name='homepage'),

]
