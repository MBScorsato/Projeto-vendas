from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('', include('link_referente_cadastro.urls')),
    path('', include('link_referente_produto.urls')),
    path('', include('link_referente_receita.urls')),
    path('', include('link_referente_cliente.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
