from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    
      url(r'^',include('crudapp.urls')),
       #url(r'^hello/',include('crudapp.urls')),
    url(r'^admin/', admin.site.urls),
]
