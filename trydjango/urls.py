from django.conf.urls import include, url
from django.contrib import admin
from oscm import urls
urlpatterns = [
    # Examples:
      url(r'^', include(urls.urlpatterns)),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
]
