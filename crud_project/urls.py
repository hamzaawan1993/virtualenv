from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^crudapp/',include('crudapp.urls')),
    url(r'^admin/', admin.site.urls),
]
