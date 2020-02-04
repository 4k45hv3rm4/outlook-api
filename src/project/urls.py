from django.conf.urls import url, include
from django.contrib import admin
from connect import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^connect/', include('connect.urls',namespace='connect')),
    url(r'^admin/', admin.site.urls),
]
