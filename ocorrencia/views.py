from ast import Pass
from base64 import decode
from dataclasses import dataclass
from django.shortcuts import redirect, render
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView,FormView

from chartjs.views.lines import BaseLineChartView

from django.views import View

from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from ocorrencia.forms import CreateOcorrenciaForm, LoginForm, LoginUsuarioForm, FiltroRelatorioOcorrencia
from ocorrencia.utils import get_descendants_users
from .models import Usuario, Ocorrencia, PassagemPlatao
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from datetime import datetime
import csv
from django.http import HttpResponse, HttpResponseRedirect, FileResponse
import io

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch


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
    paginate_by = 5
    ordering = ['id']
    queryset = Ocorrencia.objects.all()
    context_object_name = 'Ocorrencia'

class CreateOcorrenciaView(LoginRequiredClass, View):

    model = Ocorrencia
    template_name = 'ocorrencia_forms.html'
    success_url = reverse_lazy('list_ocorrencia')


def post(request):
    
    submitted = False
    template_name = 'ocorrencia_forms.html'
    
    if request.method == "POST":
        
        form = CreateOcorrenciaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add-ocorrencia?submitted=True')
    else:
        form = CreateOcorrenciaForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, template_name, {'form':form, 'submitted':submitted})


class UpdateOcorrenciaView(LoginRequiredClass,UpdateView):
    model = Ocorrencia
    template_name = 'upd_ocorrencia.html'
    fields = ('__all__')
    success_url = reverse_lazy('list_ocorrencia')


def update_ocorrencia(request, ocorrencia_id):
    ocorrencia = Ocorrencia.objects.get(pk=ocorrencia_id)
    form = CreateOcorrenciaForm(request.POST or None, instance=ocorrencia)
    if form.is_valid():
        form.save()
        return redirect('list_ocorrencia')
    return render(request, 'upd_ocorrencia2.html',
        {'ocorrencia': ocorrencia,
        'form':form})

class DetailOcorrenciaView(LoginRequiredClass,TemplateView):
    model = Ocorrencia
    template_name = 'ver_ocorrencia.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ocorrencia'] = Ocorrencia.objects.get(id=kwargs.get('id'))
        return context
class DetailPassagemView(LoginRequiredClass,TemplateView):
    model = PassagemPlatao
    template_name = 'ver_passagem.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['passagem'] = PassagemPlatao.objects.get(id=kwargs.get('id'))
        return context

class ListPassagemPlantaoView(LoginRequiredClass,ListView):
    model = PassagemPlatao
    template_name = 'list_passagem_plantao.html'
    paginate_by = 5
    ordering = ['data']
    queryset = PassagemPlatao.objects.all()
    context_object_name = 'PassagemPlatao'

class CreatePassagemPlantaoView(LoginRequiredClass,CreateView):
    model = PassagemPlatao
    template_name = 'passagem_plantao_forms.html'
    fields = '__all__'
    success_url = reverse_lazy('list_passagem_plantao')

# class ListUsuarioView(LoginRequiredClass,View):
#     model = Usuario.objects.all()
#     template_name = 'list_usuario.html'
#     paginate_by = 10
#     queryset = Usuario.objects.all()
#     context_object_name = 'usuarios'
#     form = LoginForm

#     def get(self,request):
#         form = self.form()
#         msg = None
#         users = self.model
#         return render(request,self.template_name, {
#             "form": form, 
#         "msg": msg,
#         'context_object_name':self.context_object_name,
#         'users':users})

class ListUsuarioView(LoginRequiredMixin,View):
    template_name = "list_usuario.html"
    form = LoginForm
    success_url = "/"
    segment = 'users'
    def get(self,request):
        form = self.form()
        msg = None
        users = get_descendants_users(request.user)
        return render(request,self.template_name, {
            "form": form, 
        "msg": msg,
        'segment':self.segment,
        'users':users})
  
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

class TemplateRelatorioView(LoginRequiredMixin, View):
    model = Ocorrencia
    form = FiltroRelatorioOcorrencia
    template_name = 'relatorio.html' 

    def get(self,request):

        form = self.form()

        return render(request, self.template_name, {'form': form, 'ocorrencia': Ocorrencia.objects.all()})

    def post(self,request):

        return self.relatorio_pdf(request)

        '''if request.POST.get('id'):
            if id == 'csv':
                return self.relatorio_csv(request)
        if request.POST.get('id'):
            if id == 'pdf':
                return self.relatorio_pdf(request)'''
    @staticmethod
    def relatorio_csv(request):

        id = 'csv'

        ocorrencias = Ocorrencia.objects.all()

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=ocorrencia.csv'

        writer = csv.writer(response, delimiter=';')

        tipo = request.POST.get('tipo')
        data_inicial = request.POST.get('data_inicial')
        data_final = request.POST.get('data_final')

        if tipo:
            ocorrencias = ocorrencias.filter(tipo=tipo)
        if data_inicial:
            data_inicial = datetime.strptime(data_inicial, '%Y-%m-%d')
            ocorrencias = ocorrencias.filter(data__gte=data_inicial)
        if data_final:
            data_final = datetime.strptime(data_final, '%Y-%m-%d')
            ocorrencias = ocorrencias.filter(data__lte=data_final)

        writer.writerow(['Hora/Data', 'Local', 'Tipo', 'Descrição'])

        for ocorrencia in ocorrencias:
            writer.writerow([ocorrencia.data.strftime('%d-%m-%Y %H:%M'), ocorrencia.get_centro_display(), ocorrencia.get_tipo_display(), ocorrencia.descricao])
            print(ocorrencia.data.strftime('%d-%m-%Y %H:%M'))

        return response

    @staticmethod
    def relatorio_pdf(request):

        buffer = io.BytesIO()
        p = canvas.Canvas(buffer, pagesize=letter, bottomup=0)
        
        textob = p.beginText()

        ocorrencias = Ocorrencia.objects.all()

        linhas = ["askldjaslkdj",
        "asdasd",
        "asdasaaaaaaa"]

        for line in linhas:
            textob.textLine(line)

        for ocorrencia in ocorrencias:
            linhas.append(ocorrencia.data)
            linhas.append(ocorrencia.get_centro_display())
            linhas.append(ocorrencia.get_tipo_display())
            linhas.append(ocorrencia.descricao)

        p.drawString(100,100, textob)
        p.showPage()
        p.save()

        buffer.seek(0)


        return FileResponse(buffer, as_attachment=True, filename='hello.pdf')