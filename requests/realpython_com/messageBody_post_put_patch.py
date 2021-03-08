import requests
import json # noqa


# POST, PUT, and the less common PATCH requests
# -- their data through the message body rather than through parameters in the query string
# -- Using requests, you’ll pass the payload to the corresponding function’s data parameter.

# data takes:
# -- a dictionary, -- a list of tuples,
# -- bytes, -- or a file-like object.

# to adapt the data you send in the body of your request to the specific needs of the service you’re interacting with

#
# For example, if your request’s content type is application/x-www-form-urlencoded

post_response1 = requests.post('https://httpbin.org/post', data={'key': 'value'})
print(post_response1.status_code)
print(post_response1.json()['headers']['Content-Type'])

# You can also send that same data as a list of tuples:
post_response2 = requests.post('https://httpbin.org/post', data=[('key', 'value')])
print(post_response2.status_code)
print(post_response2.json()['headers']['Content-Type'])
#
#
# JSON as data in the body message
#
# If, however, you need to send JSON data, you can use the json parameter.
# When you pass JSON data via json, requests will serialize your data and add the correct Content-Type header for you.

post_response3 = requests.post('https://httpbin.org/post', json={'key': 'value'})
json_response = post_response3.json()
print(post_response3.status_code)
print(post_response3.json()['headers']['Content-Type'])
#json_response['data']
# '{"key": "value"}'
# json_response['headers']['Content-Type']
# 'application/json'

