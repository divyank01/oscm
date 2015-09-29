from django.conf.urls import include, url

urlpatterns = [
      url(r'^$', 'oscm.views.SignIn', name='SignIn'),
]
