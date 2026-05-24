from django.urls import path
from . import views

urlpatterns = [
    path('',views.service_list,name='services_list'),
    path('<slug:slug>/',views.service_detail,name="services_detail"),

]
