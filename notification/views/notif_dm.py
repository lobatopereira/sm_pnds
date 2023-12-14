from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ukl.utils import *
from django.contrib import messages
from users.decorators import allowed_users
from ukl.models import *


@login_required
@allowed_users(allowed_roles=['dir_mun'])
def DMSurveyNotifList(request):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	obj1 = SurveyUKL.objects.filter(is_sent=True, is_approved=False,municipality__id=diretor.areamunicipality.id).all()
	objects = obj1
	context = {
		"title":"Lista Notifikasaun Survey UKL husi Postu",
		"objects":objects,
		"group":group,
		"page":"list",
	}

	return render (request, 'dir_mun/notif_survey_list.html',context)

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def notifDetailSurveyUKL(request,hashid):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	obj1 = SurveyUKL.objects.get(hashed=hashid)
	objects = obj1
	benefisiariu = BenefisiariuUKL.objects.filter(survey=objects).order_by('naran')
	benefisiariulist = list()
	for i in benefisiariu:
		implemented = ImplementasaunUKL.objects.filter(benefisiariu__id=i.id).last()
		if implemented:
			benefisiariulist.append([i,'implemented',implemented])
		else:
			benefisiariulist.append([i,'not implemented',list()])
	surveyImage = SurveyUKLImage.objects.filter(survey=objects)
	context = {
		"title":"Detallu Notifikasaun Survey UKL husi Postu",
		"objects":objects,"benefisiariu":benefisiariulist,"surveyImage":surveyImage,
		"group":group,
		"page":"detail",
	}

	return render (request, 'dir_mun/notif_survey_detail.html',context)

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def rejeitaSurvey(request):
	hashid = request.GET['hashed']
	rejeita_info = request.GET['rejeita_info']
	surveyData = get_object_or_404(SurveyUKL,hashed=hashid)
	surveyData.is_rejected = True
	surveyData.is_sent = False
	surveyData.rejected_info = rejeita_info
	surveyData.save()
	messages.success(request, f'Dadus Survey UKL iha aldeia {surveyData.aldeia}, suku {surveyData.village} Rejeita no Manda Fila ho Susesu.')
	return redirect('DMSurveyNotifList')

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def aprovaSurvey(request,hashid):
	surveyData = get_object_or_404(SurveyUKL,hashed=hashid)
	surveyData.is_rejected = False
	surveyData.is_sent = True
	surveyData.is_approved = True
	surveyData.save()
	messages.success(request, f'Dadus Survey UKL iha aldeia {surveyData.aldeia}, suku {surveyData.village} Aprova ho Susesu.')
	return redirect('notifDetailSurveyUKL',surveyData.hashed)

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def aprovaImplementasaun(request,hashid):
	implementasaunData = get_object_or_404(ImplementasaunUKL,hashed=hashid)
	implementasaunData.is_rejected = False
	implementasaunData.is_sent = True
	implementasaunData.is_approved = True
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun UKL ba benefisiariu {implementasaunData.benefisiariu.naran} iha suku {implementasaunData.village} Aprova ho Susesu.')
	return redirect('DMUKLImplementBenefNotifDetail',implementasaunData.hashed)

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def rejeitaImplementasaun(request):
	hashid = request.GET['hashed']
	rejeita_info = request.GET['rejeita_info']
	implementasaunData = get_object_or_404(ImplementasaunUKL,hashed=hashid)
	implementasaunData.is_rejected = True
	implementasaunData.is_sent = False
	implementasaunData.rejected_info = rejeita_info
	implementasaunData.save()
	messages.success(request, f'Dadus Implementasaun UKL ba benefisiariu {implementasaunData.benefisiariu.naran} iha suku {implementasaunData.village} Rejeita no Manda Fila ho Susesu.')
	return redirect('DMUKLImplementBenefNotifDetail',implementasaunData.hashed)

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def DMImplementationNotifList(request):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	obj1 = ImplementasaunUKL.objects.filter(is_sent=True, is_approved=False,municipality__id=diretor.areamunicipality.id).all()
	objects = obj1
	context = {
		"title":"Lista Notifikasaun Implementasaun UKL husi Postu",
		"objects":objects,
		"group":group,
		"page":"list",
	}

	return render (request, 'dir_mun/notif_implementation_list.html',context)


@login_required
@allowed_users(allowed_roles=['dir_mun','admpost'])
def DMUKLImplementBenefNotifDetail(request,hashid):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	# objects = SurveyUKL.objects.filter(is_sent=True, is_approved=True,municipality__id=diretor.areamunicipality.id).all()
	objects = ImplementasaunUKL.objects.get(hashed=hashid)
	implementationImage = ImplementasaunUKLImage.objects.filter(implementasaun=objects)
	context = {
		"title":f"Detallu Implementasaun Programa UKL ba Benefisiariu {objects.benefisiariu.naran}",
		"active_programa":"active",
		"page":"dash",
		"group":group,
		"objects":objects,"implementationImage":implementationImage,
	}
	return render(request, "dir_mun/notif_implementation_detail.html",context)
