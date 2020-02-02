from urllib.parse import quote, urlencode
import base64
import json
import time
import requests

client_id     = "293d9590-b9a9-44aa-80f5-1c1bcc6229e2"
client_secret = "Zdv.Zl7PyElmsQGU4K:rUu:bq[kx4pv6"

authority     = 'https://login.microsoftonline.com'

authorize_url = '{0}{1}'.format(authority, '/common/oauth2/v2.0/authorize?{0}')

token_url     = '{0}{1}'.format(authority, '/common/oauth2/v2.0/token')


scopes = [ 'openid',
           'offline_access',
           'User.Read',
           'Mail.Read' ]

def get_signin_url(redirect_url):

    params = { 'client_id': client_id,
             'redirect_url': redirect_url,
             'response_type': 'code',
             'scope': ' '.join(str(i) for i in scopes)
            }

    signin_url = authorize_url.format(urlencode(params))

    return signin_url

def get_token_from_code(auth_code, redirect_uri):
    post_data = {'grant_type'   : 'authorization_code',
                 'code'         : auth_code,
                 'redirect_uri' : redirect_uri,
                 'scope'        : ' '.join(str(i) for i in scopes),
                 'client_id'    : client_id,
                 'client_secret': client_secret,
            }
    r = requests.post(token_url, data = post_data)
    try :
        return r.json()
    except:
        return "Error retrieving token :{0} - {1}".format(r.status_code, r.text)

def get_token_from_refresh_token(refresh_token, redirect_url):
    post_data = {'grant_type':'refresh_token',
                 'refresh_token':refresh_token,
                 'redirect_url':redirect_url,
                 'scope':' '.join(str(i) for i in species),
                 'client_id':client_id,
                 'client_secret':client_secret
            }
    r = request.post(token_url, data = post_data)
    try:
        return r.json()
    except:
        return "Error retrieving token :{0} - {1}".format(r.status_code, r.text)

def get_acces_token(request, redirect_url):
    current_token = request.session['access_token']
    expiration    = request.session['token_expires']
    now = int(time.time())
    if (current_token and  now < expiration):
        return current_token
    else:
        refresh_token = request.session['refresh_token']
        new_tokens    = get_token_from_refresh_token(refresh_token)

        expiration = int(time.time()) + new_tokens['expires_in'] - 300
        request.session['access_token']  = new_tokens['access_token']
        request.session['refresh_token'] = new_tokens['refresh_token']
        request.session['token_expires'] = expiration
        return new_tokens['access_token']
