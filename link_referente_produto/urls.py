from django.urls import path
from . import views

urlpatterns = [

    path('link_referente_produto', views.link_referente_produto, name='link_referente_produto'),

]
