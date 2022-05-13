from django.urls import path


from .views import ListOcorrenciaView, CreateOcorrenciaView, LoginUsuarioView, UpdateOcorrenciaView, DetailOcorrenciaView, ListPassagemPlantaoView, CreatePassagemPlantaoView, ListUsuarioView, DadosJSONView, TemplateEstatisticaView, TemplateRelatorioView

from .views import logout_view

urlpatterns = [
    path('login/',LoginUsuarioView.as_view(),name='login_usuario'),
    path('logout/',logout_view,name='login_usuario'),
    path('list-ocorrencia/', ListOcorrenciaView.as_view(), name='list_ocorrencia'),
    path('add/', CreateOcorrenciaView.as_view(), name='add_ocorrencia'),
    path('<int:pk>/update/', UpdateOcorrenciaView.as_view(), name='upd_ocorrencia'),
    path('<int:id>/detail/', DetailOcorrenciaView.as_view(), name='det_ocorrencia'),
    path('list-passagem-plantao/', ListPassagemPlantaoView.as_view(), name='list_passagem_plantao'),
    path('add-passagem-plantao/', CreatePassagemPlantaoView.as_view(), name='add_passagem_plantao'),
    path('list-usuario/', ListUsuarioView.as_view(), name='list_usuario'),
    path('relatorio/', TemplateRelatorioView.as_view(), name='relatorio'),
    path('estatistica', TemplateEstatisticaView.as_view(), name='estatistica'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
]