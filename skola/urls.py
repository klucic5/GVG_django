from django.conf.urls import url, include
from django.contrib import admin

urlpatterns=[
	url(r'^skolaweb/',include('skolaweb.urls')),
	url(r'^admin/',admin.site.urls),
	]
