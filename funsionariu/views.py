from django.shortcuts import render,redirect, get_object_or_404,HttpResponse
from django.contrib import messages
from funsionariu.models import Funsionariu,UserFunsionariu
from .forms import FunsionariuForm,UpdateFunsionariuForm
from django.contrib.auth.models import User,Group
from custom.utils import *
from custom.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users

# Create your views here.
@login_required
@allowed_users(allowed_roles=['admin'])
def ListaFunsionariu(request):
	listaFunsionariu = Funsionariu.objects.all()
	context = {
		"title":"Lista Funsionariu PNDS",
		"active_funsionariu":"active",
		"page":"list",
		"listaFunsionariu":listaFunsionariu,
	}
	return render(request, "ListaFunsionariu.html",context)

@login_required
@allowed_users(allowed_roles=['admin'])
def AddFunsionariu(request):
	if request.method == "POST":
		_, newid = getlastid(Funsionariu)
		hashid = hash_md5(str(newid))
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = FunsionariuForm(request.POST,request.FILES)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.hashed = hashid
			instance.user_created = request.user
			if instance.tipu_f == "Diretor Nacional":
				instance.is_nac = True
				username = str("dn")+str("pnds")+str(newid)  
				group_user = Group.objects.get(name='dir_nac')
			elif instance.tipu_f == "Diretor Municipio":
				instance.is_mun = True
				mun = get_object_or_404(Municipality,id=request.POST.get('areamunicipality'))
				instance.areamunicipality = mun
				username = str("dm")+str(mun.name)+str(newid)  
				group_user = Group.objects.get(name='dir_mun')
			elif instance.tipu_f == "Funcionario Posto":
				instance.is_post = True
				mun = get_object_or_404(Municipality,id=request.POST.get('areamunicipality'))
				post = get_object_or_404(AdministrativePost,id=request.POST.get('areaadministrativepost'))
				instance.areamunicipality = mun
				instance.areaadministrativepost = post
				username = str("fp")+str(post.name)+str(newid)  
				group_user = Group.objects.get(name='admpost')
			instance.save()
			password = make_password('password')
			obj2 = User(id=newid3, username=username, password=password)  
			obj2.save()
			obj3 = UserFunsionariu.objects.create(user=obj2,funsionariu=instance,user_created=request.user,hashed=hashid2)
			user = User.objects.get(pk=newid3)
			user.groups.add(group_user)
			messages.success(request, f'Funsionariu Foun Rejistu ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = FunsionariuForm()
	context ={
		"title":"Formulariu Rejistu Funsionariu",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)

@login_required
@allowed_users(allowed_roles=['admin'])
def ajax_load_work_area(request):
	tipu_f = request.GET.get('tipu_f')
	if tipu_f == "Diretor Nacional":
		page = "dn"
		mun = None
	elif tipu_f == "Diretor Municipio":
		page = "dm"
		mun = Municipality.objects.all()
	elif tipu_f == "Funcionario Posto":
		page = "fp"
		mun = Municipality.objects.all()
	return render(request, 'loadWorkArea.html', {'mun': mun,'page': page})

@login_required
@allowed_users(allowed_roles=['admin'])
def UpdateFunsionariu(request,hashid):
	funsionariu = get_object_or_404(Funsionariu,hashed=hashid)
	if request.method == "POST":
		newid2 = getjustnewid(UserFunsionariu)
		hashid2 = hash_md5(str(newid2))
		newid3 = getjustnewid(User)
		form = UpdateFunsionariuForm(request.POST,request.FILES,instance=funsionariu)
		if form.is_valid():
			instance = form.save(commit=False)
			instance.save()
			messages.success(request, f'Dadus Funsionariu Altera ho Susesu.')
			return redirect('ListaFunsionariu')
	else:	
		form = UpdateFunsionariuForm(instance=funsionariu)
	context ={
		"title":"Formulariu Altera Dadus Funsionariu",
		"page":"form",
		"form":form,
		"active_funsionariu":"active",
	}
	return render(request,'ListaFunsionariu.html',context)