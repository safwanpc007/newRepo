from django.urls import path

from . import views

app_name='aappp'

urlpatterns = [
    # path('home',views.home),
    path('',views.customer,name='home.html'),
]
