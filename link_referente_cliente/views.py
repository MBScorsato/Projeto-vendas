from django.shortcuts import render


def link_referente_cliente(request):
    if request.method == 'GET':
        return render(request, 'link_referente_cliente.html')

    elif request.method == 'POST':
        return render(request, 'link_referente_cliente.html')