from django.shortcuts import render
from index.models import bootstrap_navbar, NavBar_Links


def index(request):
    if request.method == 'GET':
        nome_do_site = bootstrap_navbar.objects.all().order_by('-id').first()
        liks = NavBar_Links.objects.all().order_by('-id')

        return render(request, 'index.html',{
            'nome_do_site': nome_do_site,
            'liks': liks,
        })

    elif request.method == 'POST':
        return render(request, 'index.html')