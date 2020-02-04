from django.conf.urls import url
from connect import views

app_name="connect"

urlpatterns=[
    url(r'^$'         , views.home    , name='home'),
    url(r'^home/$'    , views.home    , name='home'),
    url(r'^gettoken/$', views.gettoken, name='gettoken'),
    url(r'^mail/$'    , views.mail    , name="mail"),
    url(r'^events/$'  , views.events  , name='events'),
    url(r'^contacts/$', views.contacts, name='contacts'),
]
# https://login.microsoftonline.com/common/oauth2/v2.0/authorize?
# scope=openid+User.Read+Mail.Read&response_type=code&
# client_id=293d9590-b9a9-44aa-80f5-1c1bcc6229e2&
# redirect_uri=http%3A%2F%2F127.0.0.1%3A8000%2Fconnect%2Fgettoken%2F
