from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from funsionariu.models import Funsionariu,UserFunsionariu
from ukl.models import *
from ukl.utils import *
from django.contrib.auth.models import User,Group
from custom.utils import *
from custom.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UKLDash(request):
	group = request.user.groups.all()[0].name
	if group == "admpost":
		userArea = c_user_fun(request.user)
		surveyObjects = SurveyUKL.objects.filter(administrativepost=userArea.areaadministrativepost).all().order_by('-surveyDate')
		objects1 = ImplementasaunUKL.objects.filter(survey__administrativepost__id=userArea.areaadministrativepost.id).all()
	elif group == "admin":
		surveyObjects = SurveyUKL.objects.all().order_by('-surveyDate')
		objects1 = ImplementasaunUKL.objects.filter().all()
	context = {
		"title":"Dashboard Programa UKL PNDS",
		"active_programa":"active",
		"page":"dash",
		"group":group,
		"objects1":objects1,
		"surveyObjects":surveyObjects,
	}
	return render(request, "ukldash/dash.html",context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def DetailSurveyUKL(request,hashid):
	group = request.user.groups.all()[0].name
	objects = SurveyUKL.objects.get(hashed=hashid)
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
		"title":"Detallu Survey Programa UKL",
		"active_programa":"active",
		"page":"detail",
		"group":group,
		"objects":objects,"benefisiariu":benefisiariulist,"surveyImage":surveyImage,
	}
	return render(request, "survey/detail.html",context)

@login_required
def ajax_load_detail_benefisiariu(request):
	benId = request.GET.get('benId')
	objects = get_object_or_404(BenefisiariuUKL,id=benId)
	return render(request, 'benefisiariu/ajax_load_detail_benefisiariu.html', {'objects': objects})
	

