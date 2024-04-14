from django.urls import path
from . import views

urlpatterns = [

    path('link_referente_receita', views.link_referente_receita, name='link_referente_receita'),

]
