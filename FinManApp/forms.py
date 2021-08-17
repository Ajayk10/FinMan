from django import forms
from .models import *

class JointAccountForm(forms.ModelForm):
	class  Meta:
		model = JointAccountModel
		fields = ["date_time" , "available_balance" , "amount" , "title" ,"description","month","year"]

class InHandForm(forms.ModelForm):
	class  Meta:
		model = InHandModel
		fields = ["date_time" , "available_balance" , "amount" , "title" ,"description","month","year"]

class PensionAccountForm(forms.ModelForm):
	class  Meta:
		model = PensionAccountModel
		fields = ["date_time" , "available_balance" , "amount" , "title" ,"description","month","year"]

class CSBAccountForm(forms.ModelForm):
	class  Meta:
		model = CSBAccountModel
		fields = ["date_time" , "available_balance" , "amount" , "title" ,"description","month","year"]

class MyAccountForm(forms.ModelForm):
	class  Meta:
		model = MyAccountModel
		fields = ["date_time" , "available_balance" , "amount" , "title" ,"description","month","year"]