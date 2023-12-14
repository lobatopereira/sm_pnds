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
@allowed_users(allowed_roles=['dir_mun'])
def UKLDMDash(request):
	group = request.user.groups.all()[0].name
	diretor = c_user_fun(request.user)
	objects = SurveyUKL.objects.filter(is_sent=True, is_approved=True,municipality__id=diretor.areamunicipality.id).all()
	objects1 = ImplementasaunUKL.objects.filter(survey__municipality__id=diretor.areamunicipality.id).all()
	context = {
		"title":"Dashboard Programa UKL Aprovadu",
		"active_programa":"active",
		"page":"dash",
		"group":group,
		"objects":objects,
		"objects1":objects1,
	}
	return render(request, "dm_ukl/dash.html",context)

@login_required
@allowed_users(allowed_roles=['dir_mun','admpost'])
def DMUKLImplementBenefDetail(request,hashid):
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
	return render(request, "implementation/detail.html",context)
