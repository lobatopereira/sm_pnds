from django.urls import path
from . import views

urlpatterns = [
    path('dir/mun/survey/notif/list/', views.DMSurveyNotifList, name="DMSurveyNotifList"),
    path('dir/mun/survey/notif/detail/<str:hashid>', views.notifDetailSurveyUKL, name="notifDetailSurveyUKL"),
    path('dir/mun/survey/rejects/', views.rejeitaSurvey, name="rejeitaSurvey"),
    path('dir/mun/survey/approved/<str:hashid>', views.aprovaSurvey, name="aprovaSurvey"),
    
    path('dir/mun/implementation/notif/list/', views.DMImplementationNotifList, name="DMImplementationNotifList"),
    path('dir/mun/implementation/notif/detail/<str:hashid>', views.DMUKLImplementBenefNotifDetail, name="DMUKLImplementBenefNotifDetail"),
    path('dir/mun/implementation/rejects/', views.rejeitaImplementasaun, name="rejeitaImplementasaun"),
    path('dir/mun/implementation/approved/<str:hashid>', views.aprovaImplementasaun, name="aprovaImplementasaun"),
    

    # postu
    path('fun/postu/survey/notif/list/', views.FPSurveyNotifList, name="FPSurveyNotifList"),
    path('fun/postu/implementation/notif/list/', views.FPImplementationNotifList, name="FPImplementationNotifList"),
 
]