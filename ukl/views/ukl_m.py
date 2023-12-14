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
@allowed_users(allowed_roles=['admin','admpost'])
def AddSurveyUKL(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
		_, newid = getlastid(SurveyUKL)
		hashid = hash_md5(str(newid))
		if group == "admin":
			form = SurveyUKLForm(request.POST,request.FILES)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.hashed = hashid
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Survey Programa UKL Rejistu ho Susesu.')
				return redirect('ukl-dash')
		elif group == "admpost":
			userfunsionariu = c_user_fun(request.user)
			form = SurveyUKLForm1(request.POST,request.FILES,fun=userfunsionariu)
			if form.is_valid():
				instance = form.save(commit=False)
				munisipiu = get_object_or_404(Municipality,id=userfunsionariu.areamunicipality.id)
				postu = get_object_or_404(AdministrativePost,id=userfunsionariu.areaadministrativepost.id)
				instance.municipality = munisipiu
				instance.administrativepost = postu
				instance.hashed = hashid
				instance.user_created = request.user
				instance.save()
				messages.success(request, f'Survey Programa UKL Rejistu ho Susesu.')
				return redirect('ukl-dash')

	else:	
		if group == "admin":
			form = SurveyUKLForm()
		elif group == "admpost":
			userfunsionariu = c_user_fun(request.user)
			form = SurveyUKLForm1(fun=userfunsionariu)

	context ={
		"title":"Formulariu Rejistu Survey Programa UKL",
		"page":"form",
		"form":form,"group":group,
		"active_programa":"active",
	}
	return render(request,'survey/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UpdateSurveyUKL(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(SurveyUKL,hashed=hashid)
	if request.method == "POST":
		if group == "admin":
			form = SurveyUKLForm(request.POST,request.FILES,instance=objects)
		elif group == "admpost":
			userfunsionariu = c_user_fun(request.user)
			form = SurveyUKLForm1(request.POST,request.FILES,instance=objects,fun=userfunsionariu)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Survey Programa UKL altera ho Susesu.')
			return redirect('ukl-dash')
	else:	
		if group == "admin":
			form = SurveyUKLForm(instance=objects)
		elif group == "admpost":
			userfunsionariu = c_user_fun(request.user)
			form = SurveyUKLForm1(instance=objects,fun=userfunsionariu)
	context ={
		"title":"Formulariu Altera Dadus Survey Programa UKL",
		"page":"form",
		"form":form,"group":group,
		"active_programa":"active",
	}
	return render(request,'survey/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def AddSurveyImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(SurveyUKL,hashed=hashid)
	if request.method == "POST":
		_, newid = getlastid(SurveyUKLImage)
		hashid = hash_md5(str(newid))
		form = SurveyUKLImageForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.survey = objects
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Imajen Survey Programa UKL Upload ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = SurveyUKLImageForm()
	context ={
		"title":f"Formulariu Upload Imajen Survey UKL, {objects.surveyDate}",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'survey/formImage.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UpdateSurveyImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(SurveyUKLImage,hashed=hashid)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	if request.method == "POST":
		form = SurveyUKLImageForm(request.POST,request.FILES,instance=objects1)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Imajen Survey Programa UKL Update ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = SurveyUKLImageForm(instance=objects1)
	context ={
		"title":f"Formulariu Update Imajen Survey UKL, {objects.surveyDate}",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'survey/formImage.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def DeleteSurveyImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(SurveyUKLImage,hashed=hashid)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	objects1.delete()
	messages.error(request, f'Imajen Survey Programa UKL Delete ho Susesu.')
	return redirect('DetailSurveyUKL',objects.hashed)
	
@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def SentSurvey(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(SurveyUKL,hashed=hashid)
	objects.is_sent = True
	objects.save()
	messages.success(request, f'Dadus Survey Programa UKL manda ba Dir. PNDS Munisipiu ho Susesu.')
	return redirect('DetailSurveyUKL',objects.hashed)
	

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def AddBenefisiariu(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(SurveyUKL,hashed=hashid)
	if request.method == "POST":
		_, newid = getlastid(BenefisiariuUKL)
		hashid = hash_md5(str(newid))
		form = BenefisiariuUKLForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.survey = objects
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dadus Benefisiariu UKL Rejistu ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = BenefisiariuUKLForm()
	context ={
		"title":"Formulariu Rejistu Benefisiariu Programa UKL",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'benefisiariu/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UpdateBenefisiariu(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(BenefisiariuUKL,hashed=hashid)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	if request.method == "POST":
		form = BenefisiariuUKLForm(request.POST,request.FILES,instance=objects1)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Benefisiariu UKL Altera ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = BenefisiariuUKLForm(instance=objects1)
	context ={
		"title":"Formulariu Altera Benefisiariu Programa UKL",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'benefisiariu/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UploadBenefisiariuDoc(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(BenefisiariuUKL,hashed=hashid)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	if request.method == "POST":
		_, newid = getlastid(BenefisiariuDoc)
		hashid = hash_md5(str(newid))
		form = BenefisiariuDocForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.benefisiariu = objects1
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dokuemntu Benefisiariu {objects1.naran} Upload ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = BenefisiariuDocForm()
	context ={
		"title":f"Formulariu Upload Dokuemntu Benefisiariu {objects1.naran}",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'benefisiariu/formDoc.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UpdateBenefisiariuDoc(request,hashid):
	group = request.user.groups.all()[0].name
	objects2 = get_object_or_404(BenefisiariuDoc,hashed=hashid)
	objects1 = get_object_or_404(BenefisiariuUKL,hashed=objects2.benefisiariu.hashed)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	if request.method == "POST":
		form = BenefisiariuDocForm(request.POST,request.FILES,instance=objects2)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dokuemntu Benefisiariu {objects1.naran} Update ho Susesu.')
			return redirect('DetailSurveyUKL',objects.hashed)
	else:	
		form = BenefisiariuDocForm(instance=objects2)
	context ={
		"title":f"Formulariu Update Dokuemntu Benefisiariu {objects1.naran}",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'benefisiariu/formDoc.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def DeleteBenefisiariuDoc(request,hashid):
	group = request.user.groups.all()[0].name
	objects2 = get_object_or_404(BenefisiariuDoc,hashed=hashid)
	objects1 = get_object_or_404(BenefisiariuUKL,hashed=objects2.benefisiariu.hashed)
	objects = get_object_or_404(SurveyUKL,hashed=objects1.survey.hashed)
	objects2.delete()
	messages.error(request, f'Dokumentu {objects2.name} husi benefisiariu {objects1.naran} Delete ho Susesu.')
	return redirect('DetailSurveyUKL',objects.hashed)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def AddImplementationUKL(request):
	group = request.user.groups.all()[0].name
	if request.method == "POST":
		_, newid = getlastid(ImplementasaunUKL)
		hashid = hash_md5(str(newid))
		form = ImplementasaunUKLForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dadus Foun Implementasaun Programa UKL Rejistu ho Susesu.')
			return redirect('ukl-dash')
	else:	
		form = ImplementasaunUKLForm()
	context ={
		"title":"Formulariu Rejistu Implementasaun Programa UKL",
		"page":"form",
		"form":form,"group":group,
		"active_programa":"active",
	}
	return render(request,'implementation/form.html',context)


# implementasaun
@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def FPAtualizaInfoImple(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(ImplementasaunUKL,hashed=hashid)
	if request.method == "POST":
		form = ImplementasaunUKLForm2(request.POST,request.FILES,instance=objects)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Implementasaun UKL ba benefisiariu {objects.benefisiariu.naran} atualiza ho Susesu.')
			return redirect('DMUKLImplementBenefDetail',objects.hashed)
	else:	
		form = ImplementasaunUKLForm2(instance=objects)
	context ={
		"title":"Formulariu Atualiza informasaun implementasaun Programa UKL",
		"page":"form",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'implementation/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def AddImplementationImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(ImplementasaunUKL,hashed=hashid)
	if request.method == "POST":
		_, newid = getlastid(ImplementasaunUKLImage)
		hashid = hash_md5(str(newid))
		form = ImplementasaunUKLImageForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.implementasaun = objects
			instance.hashed = hashid
			instance.user_created = request.user
			instance.save()
			messages.success(request, f'Dokumentasaun Implementasaun UKL ba benefisiariu {objects.benefisiariu.naran} upload ho Susesu.')
			return redirect('DMUKLImplementBenefDetail',objects.hashed)
	else:	
		form = ImplementasaunUKLImageForm()
	context ={
		"title":"Formulariu Upload Dokumentasaun implementasaun Programa UKL",
		"page":"impleimageform",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'implementation/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def UpdateImplementationImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(ImplementasaunUKLImage,hashed=hashid)
	objects = get_object_or_404(ImplementasaunUKL,hashed=objects1.implementasaun.hashed)
	if request.method == "POST":
		form = ImplementasaunUKLImageForm(request.POST,request.FILES,instance=objects1)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dokumentasaun Implementasaun UKL ba benefisiariu {objects.benefisiariu.naran} atualiza ho Susesu.')
			return redirect('DMUKLImplementBenefDetail',objects.hashed)
	else:	
		form = ImplementasaunUKLImageForm(instance=objects1)
	context ={
		"title":"Formulariu Atualiza Dokumentasaun implementasaun Programa UKL",
		"page":"impleimageform",
		"form":form,"group":group,"objects":objects,
		"active_programa":"active",
	}
	return render(request,'implementation/form.html',context)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def deleteImplementationImage(request,hashid):
	group = request.user.groups.all()[0].name
	objects1 = get_object_or_404(ImplementasaunUKLImage,hashed=hashid)
	objects = get_object_or_404(ImplementasaunUKL,hashed=objects1.implementasaun.hashed)
	objects1.delete()
	messages.error(request, f'Imajen Implementasaun Programa UKL Delete ho Susesu.')
	return redirect('DMUKLImplementBenefDetail',objects.hashed)

@login_required
@allowed_users(allowed_roles=['admin','admpost'])
def SentImplementation(request,hashid):
	group = request.user.groups.all()[0].name
	objects = get_object_or_404(ImplementasaunUKL,hashed=hashid)
	objects.is_sent = True
	objects.save()
	messages.success(request, f'Dadus Implementasaun Programa UKL manda ba Dir. PNDS Munisipiu ho Susesu.')
	return redirect('DMUKLImplementBenefDetail',objects.hashed)
	