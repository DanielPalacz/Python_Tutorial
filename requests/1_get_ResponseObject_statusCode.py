import requests
import json # noqa

# A Response is a powerful object for inspecting the results of the request.
get_http_response = requests.get('https://api.github.com')
# captured the return value of get(), which is an instance of 'Response', and stored it in a variable called response.
# You can now use response to see a lot of information about the results of your GET request.

#
# 1. Status code:


print(get_http_response.status_code)
get_http_response.raise_for_status()

print("Response object namespace - dir(get_http_response):")
print(dir(get_http_response))
for el in dir(get_http_response):
    print(el)

