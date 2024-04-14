from django.urls import path
from . import views

urlpatterns = [

    path('link_referente_cadastro', views.link_referente_cadastro, name='link_referente_cadastro'),

]
