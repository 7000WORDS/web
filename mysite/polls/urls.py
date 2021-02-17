from django.http import HttpResponse
from django.urls import path 

from . import views
from .models import Question


urlpatterns = [
    path ('', views.index, name = 'index'),
    path('<int:question_id/', views.detail, name='detail'),
    path('<int:question_id/results/', views.results,name= 'results'),
    path('<int:question_id>/vote/vote', views.vote, name= 'vote'),
]