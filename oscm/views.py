from django.shortcuts import render
from .models import Login
from .forms import LoginForm
import formFormatter as formatter
def SignIn(request):
	title="OSCM|Login"
	template="base.html"
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
			template="base.html"
			context['login']=False
	
	return render(request,template,context)