from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from lab_access import views


urlpatterns = [
    url(r'^alunos/$',views.AlunoList.as_view()),
    url(r'^professores/$',views.ProfessorList.as_view()),
    url(r'^tecnicos/$',views.TecnicoList.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
