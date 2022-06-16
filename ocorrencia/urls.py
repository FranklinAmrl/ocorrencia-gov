from django import views
from django.urls import path


from .views import DetailPassagemView, ListOcorrenciaView, CreateOcorrenciaView, LoginUsuarioView, UpdateOcorrenciaView, DetailOcorrenciaView, ListPassagemPlantaoView, CreatePassagemPlantaoView, ListUsuarioView, DadosJSONView, TemplateEstatisticaView, TemplateRelatorioView, post

from .views import logout_view, update_ocorrencia

urlpatterns = [
    path('login/',LoginUsuarioView.as_view(),name='login_usuario'),
    path('logout/',logout_view,name='login_usuario'),
    path('list-ocorrencia/', ListOcorrenciaView.as_view(), name='list_ocorrencia'),
    path('', ListOcorrenciaView.as_view(), name='list_ocorrencia'),
    #path('add-ocorrencia/', CreateOcorrenciaView.as_view(), name='add_ocorrencia'),
    path('add-ocorrencia/', post, name='add_ocorrencia'),
    path('<int:pk>/update/', UpdateOcorrenciaView.as_view(), name='upd_ocorrencia'),
    path('update-ocorrencia/<ocorrencia_id>', update_ocorrencia, name='upd_ocorrencia2'),
    path('<int:id>/detail/', DetailOcorrenciaView.as_view(), name='det_ocorrencia'),
    path('<int:id>/detail/', DetailPassagemView.as_view(), name='det_passagem'),
    path('list-passagem-plantao/', ListPassagemPlantaoView.as_view(), name='list_passagem_plantao'),
    path('add-passagem-plantao/', CreatePassagemPlantaoView.as_view(), name='add_passagem_plantao'),
    path('list-usuario/', ListUsuarioView.as_view(), name='list_usuario'),
    path('relatorio/', TemplateRelatorioView.as_view(), name='relatorio'),
   # path('relatorio-csv/', TemplateRelatorioView.relatorio_csv().as_view(), name='relatorio_csv'),
   # path('relatorio-pdf/', TemplateRelatorioView.relatorio_pdf().as_view(), name='relatorio_pdf'),
    path('estatistica', TemplateEstatisticaView.as_view(), name='estatistica'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
]