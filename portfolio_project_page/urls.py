from django.urls import path
from . import views

app_name = "portfolio_project_page"

urlpatterns = [
    path('', views.index, name="index"),
    path('frame-contact/', views.data_frame),
    path('<slug:page_slug>/', views.page_generate, name='page_generate'),      # generate pages from admin interface
    #path('energy-report/', views.energyreportcontain),
]