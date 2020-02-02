from django.conf.urls import url
from connect import views

app_name="connect"

urlpatterns=[
    url(r'^$'         , views.home    , name='home'),
    url(r'^home/$'    , views.home    , name='home'),
    url(r'^gettoken/$', views.gettoken, name="gettoken"),
]
