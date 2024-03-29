from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('appliances/', views.appliances_list, name='appliances'),
    path('appliances/<int:appliance_id>/', views.appliances_detail, name='detail')
]

