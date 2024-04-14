from django.shortcuts import render
from index.models import bootstrap_navbar, NavBar_Links, Apresentaca_Site


def index(request):
    if request.method == 'GET':
        nome_do_site = bootstrap_navbar.objects.all().order_by('-id').first()
        liks = NavBar_Links.objects.all().order_by('-id')[:1]

        apresenta_site = Apresentaca_Site.objects.all().order_by('-id').first()
        apresenta_site_titulo = apresenta_site.titulo
        apresenta_site_arq = apresenta_site.arq
        apresenta_site_descricao = apresenta_site.descricao

        return render(request, 'index.html', {'nome_do_site': nome_do_site, 'liks': liks,
                                              'apresenta_site_titulo':apresenta_site_titulo,
                                              'apresenta_site_arq': apresenta_site_arq,
                                              'apresenta_site_descricao': apresenta_site_descricao,
                                              })
    elif request.method == 'POST':
        return render(request, 'index.html')
