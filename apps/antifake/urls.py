from django.urls import path
from apps.antifake.views import index

urlpatterns = [
    # As rotas virão aqui depois
    path('', index, name='index')
]