

# https://realpython.com/python-requests/#authentication


# Authentication:
# - Typically, you provide the credentials to a server by passing data through the Authorization header
# ----- or a custom header defined by the service.
# - requests library provides a parameter called auth, which allows you to pass your credentials


from getpass import getpass
import requests
from requests.auth import HTTPBasicAuth


auth_get_response1 = requests.get('https://api.github.com/user', auth=('username', getpass()))

# If you try to make this request with no credentials, you’ll see that the status code is 401 Unauthorized:
# requests.get('https://api.github.com/user')
print(auth_get_response1.status_code)
input("Click Enter")

# When you pass your username and password in a tuple to the auth parameter,
# requests is applying the credentials using HTTP’s Basic access authentication scheme under the hood:
# https://en.wikipedia.org/wiki/Basic_access_authentication
# Therefore, you could make the same request by passing explicit Basic authentication credentials using HTTPBasicAuth:

auth_get_response2 = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', getpass()))
# <Response [200]>


# requests provides other methods of authentication out of the box such as:
# -- HTTPDigestAuth and
# -- HTTPProxyAuth
print(dir(requests.auth))


# You can even supply your own authentication mechanism.


# To do so, you must first create a subclass of AuthBase. Then, you implement __call__():
# import requests
# from requests.auth import AuthBase


# class TokenAuth(AuthBase):
#     """Implements a custom authentication scheme."""
#
#     def __init__(self, token):
#         self.token = token
#
#     def __call__(self, r):
#         """Attach an API token to a custom auth header."""
#         r.headers['X-TokenAuth'] = f'{self.token}'  # Python 3.6+
#         return r
#
#
# requests.get('https://httpbin.org/get', auth=TokenAuth('12345abcde-token'))

# Here,
# your custom TokenAuth mechanism receives a token, then includes that token in the X-TokenAuth header of your request.

# Bad authentication mechanisms can lead to security vulnerabilities,
# so unless a service requires a custom authentication mechanism for some reason,
# you’ll always want to use a tried-and-true auth scheme like Basic or OAuth.
