from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_access import views


urlpatterns = [
    url(r'^api/professores/$',views.ProfessorListCreate.as_view()),
    url(r'^api/professores/(?P<tag>[a-z0-9]+)/$', views.ProfessorView.as_view()),
    url(r'^professores/$', views.ProfessorViewHTML.as_view(), name='professores'),
    url(r'^professores/(?P<pk>[0-9]+)/$', views.ProfessorDetail.as_view(), name='professor-detail'),
    url(r'^professores/novo/$', views.ProfessorNew.as_view(), name='professor_new'),

    url(r'^api/tecnicos/$',views.TecnicoListCreate.as_view()),
    url(r'^api/tecnicos/(?P<tag>[a-z0-9]+)/$', views.TecnicoView.as_view()),
    url(r'^tecnicos/$', views.TecnicoViewHTML.as_view(), name='tecnicos'),
    url(r'^tecnicos/(?P<pk>[0-9]+)/$', views.TecnicoDetail.as_view(), name='tecnico-detail'),
    url(r'^tecnicos/novo/$', views.TecnicoNew.as_view(), name='tecnico_new'),

    url(r'^api/alunos/$',views.AlunoListCreate.as_view()),
    url(r'^api/alunos/(?P<tag>[a-z0-9]+)/$', views.AlunoView.as_view()),
    url(r'^api/alunos/validate/(?P<tag>[a-z0-9]+)$', views.ValidateAluno.as_view()),
    url(r'^alunos/$', views.AlunosViewHTML.as_view(), name='alunos'),
    url(r'^alunos/(?P<pk>[0-9]+)/$', views.AlunoDetail.as_view(), name='aluno-detail'),
    url(r'^alunos/novo/$', views.AlunoNew.as_view(), name='aluno_new'),

    url(r'^api/laboratorios/$',views.LaboratorioListCreate.as_view()),
    url(r'^api/laboratorios/(?P<pk>[0-9]+)/$', views.LaboratorioView.as_view()),

    url(r'^api/bancadas/$',views.BancadaListCreate.as_view()),
    url(r'^api/bancadas/(?P<pk>[0-9]+)/$', views.BancadaView.as_view()),

    url(r'^api/search/(?P<tag>[a-z0-9]+)/$', views.RetrieveAll.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
