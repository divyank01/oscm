from django.shortcuts import render

from .forms import LoginForm

def SignIn(request):
	title="OSCM|Login"
	#title = "welcome %s" %(request.user)
	form = LoginForm(request.POST or None)
	context = {
		"heading" : title,
		"form" : form,
		"login" : True
	}
	if form.is_valid():
		print request.POST
	return render(request,"base.html",context)