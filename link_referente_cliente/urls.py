from django.urls import path
from . import views

urlpatterns = [

    path('link_referente_cliente', views.link_referente_cliente, name='link_referente_cliente'),

]
