from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib.auth.models import Group,User
from django.contrib.auth.decorators import login_required
from ukl.utils import *
from django.contrib import messages
from users.decorators import allowed_users
from ukl.models import *


@login_required
@allowed_users(allowed_roles=['admpost'])
def FPSurveyNotifList(request):
	group = request.user.groups.all()[0].name
	fun = c_user_fun(request.user)
	obj1 = SurveyUKL.objects.filter(is_sent=False, is_rejected=True, is_approved=False,administrativepost__id=fun.areaadministrativepost.id).all()
	objects = obj1
	context = {
		"title":"Lista Notifikasaun Survey UKL Rejeitadu",
		"objects":objects,
		"group":group,
		"page":"list",
	}

	return render (request, 'fun_post/notif_survey_list.html',context)

@login_required
@allowed_users(allowed_roles=['admpost'])
def FPImplementationNotifList(request):
	group = request.user.groups.all()[0].name
	fun = c_user_fun(request.user)
	obj1 = ImplementasaunUKL.objects.filter(is_sent=False, is_rejected=True, is_approved=False,administrativepost__id=fun.areaadministrativepost.id).all()
	objects = obj1
	context = {
		"title":"Lista Notifikasaun Implementasaun UKL Rejeitadu",
		"objects":objects,
		"group":group,
		"page":"list",
	}

	return render (request, 'fun_post/notif_implementation_list.html',context)