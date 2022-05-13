from ast import Pass
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView

from chartjs.views.lines import BaseLineChartView

from django.views import generic

from django.urls import reverse_lazy

from random import randint


from .models import Usuario, Ocorrencia, PassagemPlatao



class ListOcorrenciaView(ListView):
    model = Ocorrencia
    template_name = 'list_ocorrencia.html'
    paginate_by = 10
    ordering = ['id']
    queryset = Ocorrencia.objects.all()
    context_object_name = 'Ocorrencia'

class CreateOcorrenciaView(CreateView):
    model = Ocorrencia
    template_name = 'ocorrencia_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_ocorrencia')

class UpdateOcorrenciaView(UpdateView):
    model = Ocorrencia
    template_name = 'ocorrencia_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_ocorrencia')


class DetailOcorrenciaView(TemplateView):
    model = Ocorrencia
    template_name = 'ver_ocorrencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocorrencia'] = Ocorrencia.objects.get(id=kwargs.get('id'))
        print(context)
        return context

class ListPassagemPlantaoView(ListView):
    model = PassagemPlatao
    template_name = 'list_passagem_plantao.html'
    paginate_by = 15
    ordering = ['data']
    queryset = PassagemPlatao.objects.all()
    context_object_name = 'PassagemPlatao'

class CreatePassagemPlantaoView(CreateView):
    model = PassagemPlatao
    template_name = 'passagem_plantao_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_passagem_plantao')

class ListUsuarioView(ListView):
    model = Usuario
    template_name = 'list_usuario.html'
    paginate_by = 10
    queryset = Usuario.objects.all()
    context_object_name = 'Usuario'

class TemplateEstatisticaView(TemplateView):
    template_name = 'estatistica.html'

class DadosJSONView(BaseLineChartView):

    

    def get_labels(self):
        labels = [
            "Período 01"
        ]

        return labels

    def get_providers(self):
        datasets = [
            "Furto",
            "Agressão",
            "Roubo"
        ]
        return datasets

    def get_data(self):

        dados = []
        for l in range(3):
            for c in range(1):
                dado = [
                    randint(1, 20),  # furto

                    randint(1, 20),  # agressao

                    randint(1, 20)  # roubo

                ]
            dados.append(dado)
        return dados

class TemplateRelatorioView(TemplateView):
    #model = Ocorrencia
    template_name = 'relatorio.html'