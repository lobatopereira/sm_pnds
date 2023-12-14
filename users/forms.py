from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, HTML
from django.contrib.auth.models import Group,User
from funsionariu.models import UserFunsionariu,Funsionariu


class DateInput(forms.DateInput):
	input_type = 'date'

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('username', css_class='form-group col-md-6 mb-0'),
				Column('email', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['naran','seksu','email','nu_telefone']
		exclude = [
			'pozisaun','aldeia','village','administrativepost','municipality','tipu_f','areamunicipality','areaadministrativepost',\
			'areavillage','image','user_created','date_created','hashed'
		]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('naran', css_class='form-group col-md-6 mb-0'),
				Column('seksu', css_class='form-group col-md-6 mb-0'),
				css_class='form-row'
			),
			Row(
				Column('email', css_class='form-group col-md-4 mb-0'),
				Column('nu_telefone', css_class='form-group col-md-4 mb-0'),
				css_class='form-row'
			),

			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

class PhotoProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Funsionariu
		fields = ['image']

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.layout = Layout(
			Row(
				Column('image', css_class='form-group col-md-6 mb-0', onchange="myFunction()"),
				css_class='form-row'
			),
			HTML(""" <center> <img id='output' width='200' /> </center> """),
			HTML(""" <div class="form-group text-right"><button class="btn btn-sm btn-success" type="submit">Save <i class="fa fa-save"></i></button> """),
			HTML(""" <span class="btn btn-sm btn-secondary"  onclick=self.history.back()><i class="fa close"></i> Cancel</span></div> """)
		)

