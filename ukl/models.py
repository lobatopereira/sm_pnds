from django.db import models
import datetime
from django.core.validators import FileExtensionValidator
from custom.models import *
from custom.utils import *
from funsionariu.models import *
from django.contrib.auth.models import User
# Create your models here.

class SurveyUKL(models.Model):
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Suku ne'ebe?")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Postu ne'ebe?")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Munisipiu ne'ebe?")
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,verbose_name="Survey iha Aldeia ne'ebe?")
	surveyDate = models.DateField(null=True,verbose_name="Data Survey")
	description = models.TextField(null=True,blank=True,verbose_name="Informasaun Adisional")
	
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	is_implemented = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

class SurveyUKLImage(models.Model):
	survey = models.ForeignKey(SurveyUKL, on_delete=models.CASCADE,null=True,verbose_name="Dadus Survey")
	image = models.ImageField(upload_to='Survey_UKL_Image', null=True,blank=True,verbose_name="Upload Imajen Survey")

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = 'Survey : {0.survey}'
		return template.format(self)

class BenefisiariuUKL(models.Model):
	survey = models.ForeignKey(SurveyUKL, on_delete=models.CASCADE,null=True,verbose_name="Dadus Survey")
	naran = models.CharField(max_length=200, null=True)
	seksu = models.CharField(choices=[('Mane','Mane'),('Feto','Feto')],max_length=10,null=True,blank=True)
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True,related_name="benefitVillage")
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True,related_name="benefitAdministrativePost")
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True,related_name="benefitMunicipality")
	nu_telefone = models.CharField(max_length=200, null=True)
	eleitoral = models.IntegerField(unique=True,null=True,verbose_name="Nu. Kartaun Eleitoral")
	image = models.ImageField(upload_to='Benefisiariu_Image', null=True,blank=True,verbose_name="Upload Fotografia Benefisiariu (Ex: .PNG or JPG)")

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def benefitDocs(self):
		return BenefisiariuDoc.objects.filter(benefisiariu=self)

	def __str__(self):
		template = ' Benefisiariu : {0.naran}'
		return template.format(self)

class BenefisiariuDoc(models.Model):
	benefisiariu = models.ForeignKey(BenefisiariuUKL,on_delete=models.CASCADE,null=True,related_name="benefitdoc")
	name = models.CharField(max_length=200, null=True)
	image = models.FileField(upload_to=upload_doc_benefit, null=True, blank=True,
			validators=[FileExtensionValidator(allowed_extensions=['jpg','png'])], verbose_name="Upload Dokumentu")
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = 'Benefisiariu : {0.benefisiariu.naran} '
		return template.format(self)	


class ImplementasaunUKL(models.Model):
	year = models.ForeignKey(AnoFiscal,on_delete=models.SET_NULL,null=True,blank=True,related_name="implementationyear",verbose_name="Ano Fiskal")
	survey = models.ForeignKey(SurveyUKL,on_delete=models.SET_NULL,null=True,blank=True,related_name="implementationsurvey")
	benefisiariu = models.OneToOneField(BenefisiariuUKL,on_delete=models.CASCADE,null=True,related_name="implementationbenefit")
	aldeia = models.ForeignKey(Aldeia, on_delete=models.CASCADE,null=True,blank=True)
	village = models.ForeignKey(Village, on_delete=models.CASCADE,null=True)
	administrativepost = models.ForeignKey(AdministrativePost, on_delete=models.CASCADE,null=True)
	municipality = models.ForeignKey(Municipality, on_delete=models.CASCADE,null=True)
	startdate = models.DateField(null=True)
	enddate = models.DateField(null=True)
	budget = models.DecimalField(default=0,decimal_places=2,max_digits=10,verbose_name="Orsamentu Projetu",null=True)
	distancemun = models.CharField(max_length=200, null=True,blank=True,verbose_name="Distansia husi Munisipiu")
	implementby = models.CharField(max_length=200, null=True,blank=True,verbose_name="Implementa husi")
	medida = models.CharField(max_length=200, null=True,blank=True,verbose_name="Medida Uma")
	statusImplementasaun = models.CharField(choices=[('Not Start','Not Start'),('On Going','On Going'),('Pending','Pending'),('Abandone','Abandone'),('Complate','Complate')],default="Not Start",max_length=30,null=True,blank=True,verbose_name="Status")
	
	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)
	description = models.TextField(null=True,blank=True)
	
	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = '{0.benefisiariu} {0.village}'
		return template.format(self)

class ImplementasaunUKLImage(models.Model):
	implementasaun = models.ForeignKey(ImplementasaunUKL, on_delete=models.CASCADE,null=True,verbose_name="Dadus Implementasaun UKL")
	image = models.ImageField(upload_to='Implementasaun_UKL', null=True,blank=True,verbose_name="Upload Imajen Implementasaun")

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = 'implementasaun : {0.implementasaun}'
		return template.format(self)

class ImplementasaunPoint(models.Model):
	survey = models.OneToOneField(SurveyUKL, on_delete=models.CASCADE, null=True,related_name="surveyLocation")
	latitude = models.CharField(max_length=20, null=True, blank=True)
	longitude = models.CharField(max_length=20, null=True, blank=True)
	image = models.ImageField(upload_to='implementationLocation', null=True,blank=True)

	def __str__(self):
		template = '{0.survey}'
		return template.format(self)

class ImplementationMonitoringUKL(models.Model):
	funsionariu = models.ForeignKey(Funsionariu, null=True, on_delete= models.SET_NULL)
	implementasaun = models.ForeignKey('ImplementasaunUKL', null=True, on_delete= models.CASCADE,related_name="implementasaun")
	pursentu_programa =models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Pursentu Implementasaun",null=True)
	pursentu_acumulativa =models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Pursentu Acumulativa",null=True)
	orsamentu_gastu = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Orsamentu Gastus",null=True,blank=True)
	orsamentu_acumulativa = models.DecimalField(decimal_places=2,max_digits=10,verbose_name="Orsamentu Acumulativa",null=True,blank=True)
	komentariu = models.TextField(null=True, blank=True)
	monitoring_date = models.DateField(auto_now_add=False)

	is_locked = models.BooleanField(default=False, null=True, blank=True)
	is_sent = models.BooleanField(default=False, null=True, blank=True)
	is_approved = models.BooleanField(default=False, null=True, blank=True)
	is_rejected = models.BooleanField(default=False, null=True, blank=True)
	rejected_info = models.TextField(null=True,blank=True)

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = '{0.implementasaun}'
		return template.format(self)

class ImplementationMonitoringUKLImage(models.Model):
	monitoring = models.ForeignKey(ImplementationMonitoringUKL, on_delete=models.CASCADE,null=True,verbose_name="Dadus Monitoring Implementasaun UKL")
	image = models.ImageField(upload_to='ImplementationMonitoringUKL', null=True,blank=True,verbose_name="Upload Imajen Monitoring Implementasaun")

	user_created =  models.ForeignKey(User, on_delete=models.CASCADE,null=True)
	date_created = models.DateTimeField(auto_now_add=True, null=True)
	hashed = models.CharField(max_length=32, null=True, blank=True)

	def __str__(self):
		template = 'monitoring : {0.monitoring}'
		return template.format(self)


