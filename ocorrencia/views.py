from ast import Pass
from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView,FormView

from chartjs.views.lines import BaseLineChartView

from django.views import generic

from django.urls import reverse_lazy

from random import randint

from django.contrib.auth.mixins import LoginRequiredMixin

from ocorrencia.forms import LoginUsuarioForm
from .models import Usuario, Ocorrencia, PassagemPlatao
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

class LoginUsuarioView(FormView):
    form_class = LoginUsuarioForm
    template_name = "login.html"
    success_url = '/list-ocorrencia'
    def post(self,request, *args, **kwargs):
        classe = super().post(request, *args, **kwargs)
        usuario = authenticate(username=request.POST['username'], password=request.POST['password'])
        if usuario:
            login(request,usuario)
            return redirect(self.success_url)
        else:
            messages.add_message(request, messages.ERROR, 'CPF e/ou senha Inválida')
            return classe

def logout_view(request):
    logout(request)
    return redirect("/login/")

class LoginRequiredClass(LoginRequiredMixin):
    login_url = "/login/"

class ListOcorrenciaView(LoginRequiredClass,ListView):
    model = Ocorrencia
    template_name = 'list_ocorrencia.html'
    paginate_by = 10
    ordering = ['id']
    queryset = Ocorrencia.objects.all()
    context_object_name = 'Ocorrencia'

class CreateOcorrenciaView(LoginRequiredClass,CreateView):
    model = Ocorrencia
    template_name = 'ocorrencia_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_ocorrencia')

class UpdateOcorrenciaView(LoginRequiredClass,UpdateView):
    model = Ocorrencia
    template_name = 'ocorrencia_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_ocorrencia')


class DetailOcorrenciaView(LoginRequiredClass,TemplateView):
    model = Ocorrencia
    template_name = 'ver_ocorrencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocorrencia'] = Ocorrencia.objects.get(id=kwargs.get('id'))
        print(context)
        return context

class ListPassagemPlantaoView(LoginRequiredClass,ListView):
    model = PassagemPlatao
    template_name = 'list_passagem_plantao.html'
    paginate_by = 15
    ordering = ['data']
    queryset = PassagemPlatao.objects.all()
    context_object_name = 'PassagemPlatao'

class CreatePassagemPlantaoView(LoginRequiredClass,CreateView):
    model = PassagemPlatao
    template_name = 'passagem_plantao_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_passagem_plantao')

class ListUsuarioView(LoginRequiredClass,ListView):
    model = Usuario
    template_name = 'list_usuario.html'
    paginate_by = 10
    queryset = Usuario.objects.all()
    context_object_name = 'Usuario'

class TemplateRelatorioView(LoginRequiredMixin,TemplateView):
    #model = Ocorrencia
    template_name = 'relatorio.html'    

class TemplateEstatisticaView(LoginRequiredClass,TemplateView):
    template_name = 'estatistica.html'

class DadosJSONView(BaseLineChartView):

    

    def get_labels(self):
        labels = [
            "Ano 2022",
        ]

        return labels

    def get_providers(self):

        datasets = Ocorrencia.get_qtd_tipo_ocorrencia().keys()

        return datasets

    def get_data(self):
        
        dados = Ocorrencia.get_qtd_tipo_ocorrencia()
        

        return dados

