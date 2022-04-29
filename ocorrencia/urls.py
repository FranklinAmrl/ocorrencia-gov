from django.urls import path


from .views import ListOcorrenciaView, CreateOcorrenciaView, UpdateOcorrenciaView, DetailOcorrenciaView, ListPassagemPlantaoView, CreatePassagemPlantaoView, ListCustomUsuarioView

urlpatterns = [
    path('list-ocorrencia/', ListOcorrenciaView.as_view(), name='list_ocorrencia'),
    path('add/', CreateOcorrenciaView.as_view(), name='add_ocorrencia'),
    path('<int:pk>/update/', UpdateOcorrenciaView.as_view(), name='upd_ocorrencia'),
    path('<int:id>/detail/', DetailOcorrenciaView.as_view(), name='det_ocorrencia'),
    path('list-passagem-plantao/', ListPassagemPlantaoView.as_view(), name='list_passagem_plantao'),
    path('add-passagem-plantao/', CreatePassagemPlantaoView.as_view(), name='add_passagem_plantao'),
    path('list-usuario/', ListCustomUsuarioView.as_view(), name='list_usuario'),
]