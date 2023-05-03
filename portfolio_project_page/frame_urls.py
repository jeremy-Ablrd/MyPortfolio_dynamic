from django.urls import path
from . import views


urlpatterns = [
    path('portfolio/frame-contact', views.data_frame),
]