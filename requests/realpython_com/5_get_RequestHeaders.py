import requests
import json

# A Response is a powerful object for inspecting the results of the request.
get_http_response = requests.get('https://api.github.com')
# captured the return value of get(), which is an instance of 'Response', and stored it in a variable called response.
# You can now use response to see a lot of information about the results of your GET request.

#
# 1. Status code:


print(get_http_response.status_code)
get_http_response.raise_for_status()


#
# 2. Content:
# how to view the actual data that the server sent back in the body of the response
# ## ## ## ## ##
# -> the payload in a variety of different formats


# 2.1. Content in bytes
print("2.1. content in bytes")
print(get_http_response.content)

#
# 2.2. Content in bytes (with def encoding)
print("2.2. content in bytes (with def encoding)")
print(get_http_response.text)


# bytes-decoding to a str requires an encoding scheme,
# requests will try to guess the encoding based on the response’s headers if you do not specify one.
# You can provide an explicit encoding by setting .encoding before accessing .text:


#
# 2.3. Content in bytes (with setuped utf-g encoding)
get_http_response.encoding = 'utf-8'
# Optional: requests infers this internally
print("2.3. content in bytes (with setuped utf-g encoding)")
print(get_http_response.text)

#
# 2.4. response.text - returns serialized JSON
print("2.4.1. get_http_response.text - returns serialized JSON")
serialized_json_response = get_http_response.text
x = json.loads(serialized_json_response)
print(serialized_json_response)
print("2.4.2. json.loads(serialized_json_response) - deserializing returned JSON")
print(x)

print("2.4.3. json.loads(serialized_json_response) - deserializing returned JSON")
print(get_http_response.json())


#
# 3. Headers
print("3. Headers")
headers = get_http_response.headers
print(headers)
for k, v in  headers.items():
    print(f"Header name: {k} - header value: {v}")
#
# The response headers can give you useful information, such as
# -- the content type of the response payload
# -- a time limit on how long to cache the response

# get_http_response.headers returns a dictionary-like object, allowing you to access header values by key

#
# 4. Query String Parameters
#
# https://api.github.com/search/repositories?q=requests+language:python
# Search GitHub's repositories for requests
response1 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
)
print()
print(response1.url)

# You can pass params to get() in the form of a dictionary, as you have just done, or as a list of tuples:
response2 = requests.get(
     'https://api.github.com/search/repositories',
     params=[('q', 'requests+language:python')],
)


#
# 5. Request Headers
#
# Customize request Headers

response3 = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

print(" 5. Request Headers")
input("response2_items will be printed:")
response2_items = response2.json()["items"]
print(response2_items[0]["text_matches"])
print(len(response2_items))
print()
input("response3_items will be printed:")
response3_items = response3.json()["items"]
print(response3_items[0]["text_matches"])
print(len(response3_items))
