from django import forms

from .models import Login

#this will only represent fields from signupmodel later on this will be passed to view thn to template
class SignUpForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = ["userName","password","role"]
		#can also exclude thingslike below
		#exclude = ["things"]

	def clean_f_name(self):
		f_name = self.cleaned_data.get("userName")

		#can validate here
		#for exceptions raise it like below
		# raise forms.validationError("this is invalid")
		return f_name

class SignUpFormV2(forms.Form):
	firstName = forms.CharField()
	lastName = forms.CharField()
	userName = forms.CharField()
	password = forms.CharField(
		widget = forms.PasswordInput()
		)
	email = forms.EmailInput()
	roles=(('admin',"Admin"),('s_user',"Super User"),('user',"User"))
	role = forms.CharField()

	def clean_firstName(self):
		f_name = self.cleaned_data.get("firstName")

		#can validate here
		#for exceptions raise it like below
		# raise forms.validationError("this is invalid")
		return f_name

class LoginForm(forms.Form):
	#class Meta:
	#	model = Login
	#	fields = ["userName","password"]
	userName=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
		# widgets = {
		# 	'userName': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}),
		# 	'password': ,
		# 	#'role': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Role'}),
		# }
		# labels = {
  #           'userName': '',
  #           'password': '',
  #           #'role': '',
  #       }
	def clean_userName(self):
		userName = self.cleaned_data.get("userName")
		return userName
		#model.role.choices[0]="select"
