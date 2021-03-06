from django import forms

from .models import Login, User, Case

from .constants import Dropdowns

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

class CreateUserForm(forms.Form):
	userName=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
	password=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
	firstName=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'FirstName'}))
	lastName=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'LastName'}))
	email=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email','type':'email'}))
	roles=(('admin',"Admin"),('super_user',"Super User"),('user',"User"))
	role=forms.ChoiceField(choices=roles,widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Role'}))

class CaseForm(forms.Form):
	class PersonalInfo(forms.Form):
		name=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name'}))
		sexes=(('Male','Male'),('Female','Female'))
		#sex=forms.CharField(widget=forms.RadioSelect(attrs={'class': 'form-control','style':'height:auto'},choices=sexes))
		sex=forms.CharField(widget=forms.RadioSelect(attrs={'class': ''},choices=sexes))
		current_age=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		age_at_addmission=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		case=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		religion=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		residential_status=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		district=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		state=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		residential_details=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		who_brought_child_to_childeren_welfare_commity=forms.CharField(widget=forms.Select(attrs={'class': 'form-control','style':'height:auto'},choices=Dropdowns.PersonalDetails.bringer_to_welfare))
		reasons_for_leaving_family=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'UserName'}))
		misbehaviour_against_child=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Dropdowns.PersonalDetails.misbehaviours))
	class PersonalInfo2(forms.Form):
		types_of_abuses=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Dropdowns.PersonalDetails.abuses))
		child_abuse=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Dropdowns.PersonalDetails.child_abuse))
		suffering_for_diseases_or_disorders=forms.CharField(widget=forms.CheckboxSelectMultiple(choices=Dropdowns.PersonalDetails.diseases))
		before_addmission_living_with=forms.CharField(widget=forms.Select(attrs={'class': 'form-control'},choices=Dropdowns.PersonalDetails.living_with))
	personal1=PersonalInfo()
	personal2=PersonalInfo2()
