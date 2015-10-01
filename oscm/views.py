from django.shortcuts import render
from .models import Login
from .forms import LoginForm, CreateUserForm
import formFormatter as formatter
def SignIn(request):
	title="OSCM|Login"
	template="login.html"
	#title = "welcome %s" %(request.user)
	form = LoginForm(request.POST or None)
	print form.errors
	context = {
		"heading" : title,
		"form" : form,
		"login" : True
	}
	if form.is_valid():
		print "valid"
		login = Login.objects.get(userName=form.cleaned_data.get('userName'))
		print login.password+"---"
		print form.cleaned_data.get('password')+"++"
		if login.password == form.cleaned_data.get('password'):
			template="home.html"
			context['login']=False
	
	return render(request,template,context)

def CreateUser(request):
	title="OSCM|New user"
	template="createUser.html"
	#title = "welcome %s" %(request.user)
	form = CreateUserForm(request.POST or None)
	print form.errors
	context = {
		"heading" : title,
		"form" : form,
		"login" : False
	}
	if form.is_valid():
		print "valid"
		# login = Login.objects.get(userName=form.cleaned_data.get('userName'))
		# print login.password+"---"
		# print form.cleaned_data.get('password')+"++"
		# if login.password == form.cleaned_data.get('password'):
		# 	template="home.html"
		# 	context['login']=False
	
	return render(request,template,context)

def CreateCase(request):
	title="OSCM|New user"
	template="newCase.html"
	#title = "welcome %s" %(request.user)
	form = CreateUserForm(request.POST or None)
	print form.errors
	context = {
		"heading" : title,
		"form" : form,
		"login" : False
	}
	if form.is_valid():
		print "valid"
		# login = Login.objects.get(userName=form.cleaned_data.get('userName'))
		# print login.password+"---"
		# print form.cleaned_data.get('password')+"++"
		# if login.password == form.cleaned_data.get('password'):
		# 	template="home.html"
		# 	context['login']=False
	
	return render(request,template,context)