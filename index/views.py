from django.shortcuts import render

#grgbttyny
def index(request):
    if request.method == 'GET':
        return render(request, 'index.html')
    elif request.method == 'POST':
        return render(request, 'index.html')