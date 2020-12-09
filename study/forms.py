from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from study.models import *



class UserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','email','password1','password2']


class StaffForm(UserCreationForm):
	class Meta:
		model = User
		fields =  ['username','password1','password2','email','is_staff']


class Selectform(ModelForm):
	class Meta:
		model = Select
		fields= ['Class','Subject']

		widgets={
				'Class':forms.Select(attrs={'class':'form-control','placeholder':'Select Class'}),
				'Subject':forms.Select(attrs={'class':'form-control','placeholder':'Select Subject'}),

		}


class Tl6form(ModelForm):
	class Meta:
		model = T6M
		fields="__all__"

		widgets={
				'video':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter video Url'}),
				'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter video title'}),

		}


class Hl6form(ModelForm):
	class Meta:
		model = H6M
		fields="__all__"

class El6form(ModelForm):
	class Meta:
		model = E6M
		fields="__all__"

class Ml6form(ModelForm):
	class Meta:
		model = M6M
		fields="__all__"


class Sl6form(ModelForm):
	class Meta:
		model = S6M
		fields="__all__"

class Scl6form(ModelForm):
	class Meta:
		model = Sc6M
		fields="__all__"














# from study.models import Register,Login

# class Registerform(ModelForm):
# 	class Meta:
# 		model = Register
# 		fields = "__all__"


# class Loginform(ModelForm):
# 	class Meta:
# 		model = Login
# 		fields = "__all__" 