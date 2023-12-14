from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from funsionariu.models import Funsionariu,UserFunsionariu
from ukl.models import *
from ukl.forms import *
from ukl.utils import c_user_fun
from django.contrib.auth.models import User,Group
from custom.utils import *
from custom.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users

@login_required
@allowed_users(allowed_roles=['dir_mun'])
def DMUKLImplementBenef(request,hashid):
	group = request.user.groups.all()[0].name
	benefisiariu = get_object_or_404(BenefisiariuUKL,hashed=hashid)
	survey = get_object_or_404(SurveyUKL,hashed=benefisiariu.survey.hashed)
	if request.method == "POST":
		_, newid = getlastid(ImplementasaunUKL)
		hashid = hash_md5(str(newid))
		form = ImplementasaunUKLForm1(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.benefisiariu = benefisiariu
			instance.survey = survey
			mun = get_object_or_404(Municipality,id=survey.municipality.id)
			post = get_object_or_404(AdministrativePost,id=survey.administrativepost.id)
			vill = get_object_or_404(Village,id=survey.village.id)
			ald = get_object_or_404(Aldeia,id=survey.aldeia.id)
			instance.municipality = mun
			instance.administrativepost = post
			instance.village = vill
			instance.aldeia = ald
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Implementasaun Programa UKL ba benefisiariu {benefisiariu.naran} Rejistu ho Susesu.')
			return redirect('notifDetailSurveyUKL',benefisiariu.survey.hashed)
	else:	
		form = ImplementasaunUKLForm1()

	context ={
		"title":f"Formulariu Implementasaun Programa UKL, Benefisiariu {benefisiariu.naran}",
		"page":"dmimpleform",
		"form":form,"group":group,"benefisiariu":benefisiariu,
		"active_programa":"active",
	}
	return render(request,'implementation/form.html',context)