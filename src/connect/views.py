from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse
from connect.authhelper import get_signin_url
from connect.outlookservice import get_me


def home(request):
    redirect_url = request.build_absolute_uri(reverse('connect:gettoken'))
    sign_in_url  = get_signin_url(redirect_url)
    context      = {'signin_url':sign_in_url}
    return render(request, 'connect/home.html', context)


def gettoken(request):

    auth_code     = request.GET['code']
    redirect_url  = request.build_absolute_uri(reverse('connect:gettoken'))
    token         = get_token_from_code(auth_code, redirect_url)
    access_token  = token['access_token']
    user          = get_me(access_token)
    refresh_token = token['refresh_token']
    expires_in    = token['expires_in']

    expiration = int(time.time())+ expires_in-300

    request.session['access_token']  = access_token
    request.session['refresh_token'] = refresh_token
    request.session['token_expires'] = expiration

    return HttpResponse('User: {0}, Access token: {1}'.format(user['displayName'], access_token))
