from django.shortcuts import render


def link_referente_cadastro(request):
    if request.method == 'GET':
        return render(request, 'link_referente_cadastro.html')

    elif request.method == 'POST':
        return render(request, 'link_referente_cadastro.html')
