from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,Group
from custom.utils import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from users.decorators import allowed_users
# Create your views here.

@login_required
def home(request):
	context= {
	}

	return render (request, 'index/indexAdmin.html',context)