from django.urls import path
from . import views


urlpatterns = [
    path('frame-contact', views.frame),
]