from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_access import views


urlpatterns = [
    # url(r'^professores/$',views.ProfessorListCreate.as_view()),
    url(r'^professores/(?P<tag>[a-z0-9]+)/$', views.ProfessorView.as_view()),
    url(r'^professores/$', views.ProfessorViewHTML.as_view(), name='professores'),

    url(r'^tecnicos/$',views.TecnicoListCreate.as_view()),
    url(r'^tecnicos/(?P<tag>[a-z0-9]+)/$', views.TecnicoView.as_view()),

    url(r'^alunos/$',views.AlunoListCreate.as_view()),
    url(r'^alunos/(?P<tag>[a-z0-9]+)/$', views.AlunoView.as_view()),
    url(r'^alunos/validate/(?P<tag>[a-z0-9]+)$', views.ValidateAluno.as_view()),

    url(r'^laboratorios/$',views.LaboratorioListCreate.as_view()),
    url(r'^laboratorios/(?P<pk>[0-9]+)/$', views.LaboratorioView.as_view()),

    url(r'^bancadas/$',views.BancadaListCreate.as_view()),
    url(r'^bancadas/(?P<pk>[0-9]+)/$', views.BancadaView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
