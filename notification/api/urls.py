from django.urls import path
from . import views

urlpatterns = [
    path('badge/dir/mun/', views.APINotifBadgeDirMun.as_view()),
    path('survey/dir/mun/', views.APINotifSurveyDirMun.as_view()),
    path('implementation/dir/mun/', views.APINotifImplementasaunDirMun.as_view()),
    
    # adminpostu
    path('badge/funsionariu/postu/', views.APINotifBadgeFunPost.as_view()),
    path('survey/rejeitadu/funsionariu/postu/', views.APINotifSurveyRejeitaduFunPost.as_view()),
    path('implementasaun/rejeitadu/funsionariu/postu/', views.APINotifImplementasaunRejeitaduFunPost.as_view()),
 
]