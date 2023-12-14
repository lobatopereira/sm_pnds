from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from .models import *
from custom.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class DateInput(forms.DateInput):
	input_type = 'date'

class SurveyUKLForm(forms.ModelForm):
	surveyDate = forms.DateField(label='Data Survey', widget=DateInput(), required=True)
	description = forms.CharField(label="Observasaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = SurveyUKL
		fields = ['surveyDate','aldeia','municipality','administrativepost','village','description']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('municipality', css_class='form-group col-md-6 mb-0'),
				Column('administrativepost', css_class='form-group col-md-6 mb-0'),
				Column('village', css_class='form-group col-md-6 mb-0'),
				Column('aldeia', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('surveyDate', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-8 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class SurveyUKLForm1(forms.ModelForm):
	surveyDate = forms.DateField(label='Data Survey', widget=DateInput(), required=True)
	description = forms.CharField(label="Observasaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = SurveyUKL
		fields = ['surveyDate','aldeia','village','description']
		exclude = ['municipality','administrativepost','user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		fun = kwargs.pop('fun',None)
		super().__init__(*args, **kwargs)
		self.fields['village'].queryset = Village.objects.filter(administrativepost__id=fun.areaadministrativepost.id).all()
		self.fields['aldeia'].queryset = Aldeia.objects.none()
		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('village', css_class='form-group col-md-6 mb-0'),
				Column('aldeia', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('surveyDate', css_class='form-group col-md-4 mb-0'),
				Column('description', css_class='form-group col-md-8 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class BenefisiariuUKLForm(forms.ModelForm):
	class Meta:
		model = BenefisiariuUKL
		fields = ['naran','seksu','municipality','administrativepost','village','eleitoral','nu_telefone','image','aldeia']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		

		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('naran', css_class='form-group col-md-6 mb-0'),
				Column('seksu', css_class='form-group col-md-6 mb-0'),
				Column('eleitoral', css_class='form-group col-md-6 mb-0'),
				Column('nu_telefone', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('municipality', css_class='form-group col-md-3 mb-0'),
				Column('administrativepost', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				Column('aldeia', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class SurveyUKLImageForm(forms.ModelForm):
	class Meta:
		model = SurveyUKLImage
		fields = ['image']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['image'].required = True
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class BenefisiariuDocForm(forms.ModelForm):
	class Meta:
		model = BenefisiariuDoc
		fields = ['name','image']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['image'].required = True
		self.fields['name'].required = True
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('name', css_class='form-group col-md-12 mb-0'),
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)




class ImplementasaunUKLForm(forms.ModelForm):
	startdate = forms.DateField(label='Data Hahu', widget=DateInput(), required=True)
	enddate = forms.DateField(label='Data Remata', widget=DateInput(), required=True)
	description = forms.CharField(label="Observasaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = ImplementasaunUKL
		fields = ['year','benefisiariu','startdate','enddate','budget','distancemun','implementby','medida','statusImplementasaun','municipality','administrativepost','village','aldeia','description']
		exclude = ['user_created','hashed','date_created','survey']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['municipality'].queryset = Municipality.objects.all()
		self.fields['administrativepost'].queryset = AdministrativePost.objects.none()
		self.fields['village'].queryset = Village.objects.none()
		self.fields['aldeia'].queryset = Village.objects.none()
		if 'municipality' in self.data:
			try:
				municipality = int(self.data.get('municipality'))
				self.fields['administrativepost'].queryset = AdministrativePost.objects.filter(municipality__id=municipality).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['administrativepost'].queryset = self.instance.municipality.administrativepost_set.order_by('name')

		if 'administrativepost' in self.data:
			try:
				administrativepost = int(self.data.get('administrativepost'))
				self.fields['village'].queryset = Village.objects.filter(administrativepost__id=administrativepost).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['village'].queryset = self.instance.administrativepost.village_set.order_by('name')

		if 'village' in self.data:
			try:
				village = int(self.data.get('village'))
				self.fields['aldeia'].queryset = Aldeia.objects.filter(village__id=village).order_by('name')
			except (ValueError, TypeError):
				pass
		elif self.instance.pk:
			self.fields['aldeia'].queryset = self.instance.village.aldeia_set.order_by('name')

		ImplementedBenefisiariu = ImplementasaunUKL.objects.values('benefisiariu__id')
		self.fields['benefisiariu'].queryset = BenefisiariuUKL.objects.filter(survey__is_approved=True).exclude(id__in=ImplementedBenefisiariu).order_by('naran')
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('benefisiariu', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML("""<div id="DetailBenefisiariu"></div>"""),
			Row(
				Column('year', css_class='form-group col-md-4 mb-0'),
				Column('startdate', css_class='form-group col-md-4 mb-0'),
				Column('enddate', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('municipality', css_class='form-group col-md-3 mb-0'),
				Column('administrativepost', css_class='form-group col-md-3 mb-0'),
				Column('village', css_class='form-group col-md-3 mb-0'),
				Column('aldeia', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('medida', css_class='form-group col-md-3 mb-0'),
				Column('budget', css_class='form-group col-md-3 mb-0'),
				Column('distancemun', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('implementby', css_class='form-group col-md-6 mb-0'),
				Column('statusImplementasaun', css_class='form-group col-md-6 mb-0'),
				Column('description', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class ImplementasaunUKLForm1(forms.ModelForm):
	startdate = forms.DateField(label='Data Hahu', widget=DateInput(), required=True)
	enddate = forms.DateField(label='Data Remata', widget=DateInput(), required=True)
	description = forms.CharField(label="Observasaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = ImplementasaunUKL
		fields = ['year','startdate','enddate','budget','description']
		exclude = ['user_created','hashed','date_created','survey','benefisiariu','distancemun','implementby','medida','statusImplementasaun','municipality','administrativepost','village','aldeia']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('year', css_class='form-group col-md-4 mb-0'),
				Column('startdate', css_class='form-group col-md-4 mb-0'),
				Column('enddate', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('budget', css_class='form-group col-md-3 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('description', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class ImplementasaunUKLForm2(forms.ModelForm):
	# description = forms.CharField(label="Observasaun", required=False, widget=SummernoteWidget(attrs={'summernote': {'width': '100%', 'height': '300px'}}))
	class Meta:
		model = ImplementasaunUKL
		fields = ['distancemun','implementby','medida','statusImplementasaun','description']
		exclude = ['user_created','hashed','date_created','survey','benefisiariu','year','startdate','enddate','budget','municipality','administrativepost','village','aldeia']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('distancemun', css_class='form-group col-md-6 mb-0'),
				Column('implementby', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('medida', css_class='form-group col-md-6 mb-0'),
				Column('statusImplementasaun', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('description', css_class='form-group col-md-12 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)


class ImplementasaunUKLImageForm(forms.ModelForm):
	class Meta:
		model = ImplementasaunUKLImage
		fields = ['image']
		exclude = ['user_created','hashed','date_created']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.fields['image'].required = True
		self.helper.form_method = 'post'
		self.helper.layout = Layout(
			Row(
				Column('image', css_class='form-group col-md-12 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)