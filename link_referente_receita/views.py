from django.shortcuts import render


def link_referente_receita(request):
    if request.method == 'GET':
        return render(request, 'link_referente_receita.html')

    elif request.method == 'POST':
        return render(request, 'link_referente_receita.html')