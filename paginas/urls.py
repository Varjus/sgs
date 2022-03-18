from django.urls import path
from .views import PaginaInicial, HomePageView
from django.contrib.auth import views as auth_views
from . import views
from .views import UsuariosCreate

app_name = "paginas"

urlpatterns = [
    path('', PaginaInicial.as_view(), name='index'),
    path('sgs', HomePageView.as_view(), name='home'),
    path('', auth_views.LoginView.as_view(template_name='account/login.html'), name='cadastrar'),
    path('usuario', UsuariosCreate.as_view(), name="usuario"),
    
    
    
    
]
