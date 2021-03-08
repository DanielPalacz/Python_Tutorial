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
# 2.2. Content as text (with def encoding)
print("2.2. content in bytes (with def encoding)")
print(get_http_response.text)


# bytes-decoding to a str requires an encoding scheme,
# requests will try to guess the encoding based on the response’s headers if you do not specify one.
# You can provide an explicit encoding by setting .encoding before accessing .text:


#
# 2.3. Content as text (with setuped utf-g encoding)
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
