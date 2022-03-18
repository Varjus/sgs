from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .forms import UsuarioForm
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from .forms import UsuarioForm

class PaginaInicial(TemplateView):
    template_name = "index.html"

    def index(request):
        return render(request, 'index.html')

    

class HomePageView(TemplateView):
    template_name = "home.html"

    def index(request):
        return render(request, 'home.html')


class UsuariosCreate(CreateView):
    template_name = 'usuario.html'
    form_class = UsuarioForm
    success_url = reverse_lazy('paginas:home')

    def form_valid(self, form):

        grupo = get_object_or_404(Group, name='Usuarios')

        url = super().form_valid(form)

        self.object.groups.add(grupo)
        self.object.save()

        Usuarios.objects.create(username=self.object)

        return url

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['titulo'] = "Registro de Novo Usuário"
        context['Botao'] = "Cadastrar"
        return context