import requests
import json # noqa


# When you make a request,
# the requests library prepares the request before actually sending it to the destination server
# Request preparation includes things like validating headers and serializing JSON content.
# You can view the PreparedRequest by accessing .request:

response = requests.post('https://httpbin.org/post', json={'key': 'value'})
print(response.request.headers['Content-Type'])
print()
# 'application/json'

# PreparedRequest accessing by .request:
print("PreparedRequest accessing by '.request'.")
print("----------------------------------------")
#
print("--- response.request.url:")
print(response.request.url)
# 'https://httpbin.org/post'
print("--- response.request.body:")
print(response.request.body)
# b'{"key": "value"}'
print("--- response.request.headers:")
print(response.request.headers)
# {'User-Agent': 'python-requests/2.25.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Content-Length': '16', 'Content-Type': 'application/json'}
print("----------------------------------------")
