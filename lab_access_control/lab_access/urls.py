from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_access import views


urlpatterns = [

    url(r'^api/usuarios/$',views.UsuarioListCreate.as_view()),
    url(r'^api/usuarios/(?P<pk>[0-9]+)/$', views.UsuarioView.as_view()),
    url(r'^usuarios/$', views.UsuariosViewHTML.as_view(), name='usuarios'),
    url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view(), name='usuario-detail'),
    url(r'^usuarios/novo/$', views.UsuarioNew.as_view(), name='usuario_new'),
    url(r'^professores/$', views.ProfessorViewHTML.as_view(), name='professores'),
    url(r'^tecnicos/$', views.TecnicoViewHTML.as_view(), name='tecnicos'),

    url(r'^api/alunos/$',views.AlunoListCreate.as_view()),
    url(r'^api/alunos/(?P<tag>[a-z0-9]+)/$', views.AlunoView.as_view()),
#    url(r'^api/alunos/validate/(?P<tag>[a-z0-9]+)$', views.ValidateAluno.as_view()),
    url(r'^alunos/$', views.AlunosViewHTML.as_view(), name='alunos'),
    url(r'^alunos/(?P<pk>[0-9]+)/$', views.AlunoDetail.as_view(), name='aluno-detail'),
    url(r'^alunos/novo/$', views.AlunoNew.as_view(), name='aluno_new'),

    url(r'^api/laboratorios/$',views.LaboratorioListCreate.as_view()),
    url(r'^api/laboratorios/(?P<pk>[0-9]+)/$', views.LaboratorioView.as_view()),

    url(r'^api/bancadas/$',views.BancadaListCreate.as_view()),
    url(r'^api/bancadas/(?P<pk>[0-9]+)/$', views.BancadaView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
