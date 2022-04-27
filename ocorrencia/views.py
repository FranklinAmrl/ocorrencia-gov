from ast import Pass
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy


from .models import Ocorrencia, PassagemPlatao


class ListOcorrenciaView(ListView):
    model = Ocorrencia
    template_name = 'list_ocorrencia.html'
    paginate_by = 15
    ordering = ['data']
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
    template_name = 'ocorrencia.html'

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
    template_name = 'passagem_plantao_form.html'
    fields = '__all__'
    success_url = reverse_lazy('list_passagem_plantao')