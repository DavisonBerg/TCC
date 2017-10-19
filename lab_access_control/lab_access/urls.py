from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_access import views


urlpatterns = [
    url(r'^professores/$',views.ProfessorList.as_view()),
    url(r'^professores/create/$', views.ProfessorCreate.as_view()),
    url(r'^professores/update/(?P<pk>[0-9]+)/$', views.ProfessorUpdate.as_view()),
    url(r'^professores/delete/(?P<pk>[0-9]+)/$', views.ProfessorDelete.as_view()),

    url(r'^tecnicos/$',views.TecnicoList.as_view()),
    url(r'^tecnicos/create/$', views.TecnicoCreate.as_view()),
    url(r'^tecnicos/update/(?P<pk>[0-9]+)/$', views.TecnicoUpdate.as_view()),
    url(r'^tecnicos/delete/(?P<pk>[0-9]+)/$', views.TecnicoDelete.as_view()),

    url(r'^alunos/$',views.AlunoList.as_view()),
    url(r'^alunos/create/$', views.AlunoCreate.as_view()),
    url(r'^alunos/update/(?P<pk>[0-9]+)/$', views.AlunoUpdate.as_view()),
    url(r'^alunos/delete/(?P<pk>[0-9]+)/$', views.AlunoDelete.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
