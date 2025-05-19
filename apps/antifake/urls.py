from django.urls import path
from apps.antifake.views import home, login,cadastro_usuario, logout_usuario

urlpatterns = [
    # As rotas virão aqui depois
    path('', home, name='home'),
    path('login/', login, name='login'),
    path('cadastro/', cadastro_usuario, name='cadastro'),
    path('logout/', logout_usuario, name='logout'),
]