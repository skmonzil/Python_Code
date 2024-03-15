#from django.conf.urls import url
from django.urls import path 
from frist_app import views


from django.urls import path
from .views import home

urlpatterns = [
  
  path('', views.home, name='home'),
 

]