from django.urls import path

from . import views

app_name = 'hello'
urlpatterns = [
    #path('', views.SesAsign, name='mainpage'),
    path('', views.tryII.as_view(), name='mainpage'),
]