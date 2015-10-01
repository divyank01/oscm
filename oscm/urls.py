from django.conf.urls import include, url

urlpatterns = [
      url(r'^$', 'oscm.views.SignIn', name='SignIn'),
      url(r'^newUser/', 'oscm.views.CreateUser', name='CreateUser'),
      url(r'^newCase/', 'oscm.views.CreateCase', name='CreateCase'),
]
