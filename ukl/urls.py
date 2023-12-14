from django.urls import path
from . import views

urlpatterns = [
    path('dash/', views.UKLDash, name="ukl-dash"),
    
    # survey
    path('survey/add', views.AddSurveyUKL, name="AddSurveyUKL"),
    path('survey/update/<str:hashid>', views.UpdateSurveyUKL, name="UpdateSurveyUKL"),
    path('survey/detail/<str:hashid>', views.DetailSurveyUKL, name="DetailSurveyUKL"),
    path('survey/sent/<str:hashid>', views.SentSurvey, name="SentSurvey"),
    # survey image
    path('survey/image/upload/<str:hashid>', views.AddSurveyImage, name="AddSurveyImage"),
    path('survey/image/update/<str:hashid>', views.UpdateSurveyImage, name="UpdateSurveyImage"),
    path('survey/image/delete/<str:hashid>', views.DeleteSurveyImage, name="DeleteSurveyImage"),

    # survey benefisiariu
    path('survey/benefisiariu/add/<str:hashid>', views.AddBenefisiariu, name="AddBenefisiariu"),
    path('survey/benefisiariu/update/<str:hashid>', views.UpdateBenefisiariu, name="UpdateBenefisiariu"),
    path('survey/benefisiariu/upload/doc/<str:hashid>', views.UploadBenefisiariuDoc, name="UploadBenefisiariuDoc"),
    path('survey/benefisiariu/update/doc/<str:hashid>', views.UpdateBenefisiariuDoc, name="UpdateBenefisiariuDoc"),
    path('survey/benefisiariu/delete/doc/<str:hashid>', views.DeleteBenefisiariuDoc, name="DeleteBenefisiariuDoc"),

    # atualiza info implementasaun
    path('implementation/benefisiariu/info/update/<str:hashid>', views.FPAtualizaInfoImple, name="FPAtualizaInfoImple"),
    path('implementation/benefisiariu/doc/add/<str:hashid>', views.AddImplementationImage, name="AddImplementationImage"),
    path('implementation/benefisiariu/doc/update/<str:hashid>', views.UpdateImplementationImage, name="UpdateImplementationImage"),
    path('implementation/benefisiariu/doc/delete/<str:hashid>', views.deleteImplementationImage, name="deleteImplementationImage"),
    path('implementation/benefisiariu/implementation/info/sent/<str:hashid>', views.SentImplementation, name="SentImplementation"),

    # implementation benefisiariu
    path('implementation/add', views.AddImplementationUKL, name="AddImplementationUKL"),

    # loading
    path('load/benefisiariu/detail', views.ajax_load_detail_benefisiariu, name="ajax_load_detail_benefisiariu"),

    # dir munisipiu
    path('dir/mun/dash/', views.UKLDMDash, name="dirmun-ukl-dash"),
    path('dir/mun/implementation/benefisiariu/<str:hashid>', views.DMUKLImplementBenef, name="implementa-ukl-benef"),
    path('dir/mun/implementation/benefisiariu/detail/<str:hashid>', views.DMUKLImplementBenefDetail, name="DMUKLImplementBenefDetail"),


]