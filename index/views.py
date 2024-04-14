from django.shortcuts import render
from index.models import bootstrap_navbar


def index(request):
    if request.method == 'GET':
        ultimo_objeto_salvo = bootstrap_navbar.objects.all().order_by('-id').first()
        return render(request, 'index.html',{
            'ultimo_objeto_salvo': ultimo_objeto_salvo,
        })
    elif request.method == 'POST':
        return render(request, 'index.html')