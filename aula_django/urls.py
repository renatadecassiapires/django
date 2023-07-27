# arquivo urls usado para crirar rotas para as nossas aplicações

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/', include('autenticacao.urls')),
  
]
