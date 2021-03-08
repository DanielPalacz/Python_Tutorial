import requests


# requests Features like:
# timeout control, sessions, and retry limits
# ---> can help you keep your application running smoothly


# Timeouts

# By default, # requests waits indefinitely on the response,
# so you should rather specify a timeout duration to prevent these things from happening.

# To set the request’s timeout, use the timeout parameter.
# timeout can be an integer or float representing the number of seconds to wait on a response before timing out:
get_response_timeout1 = requests.get('https://api.github.com', timeout=1)
get_response_timeout2 = requests.get('https://api.github.com', timeout=3.05)

# You can also pass a tuple to timeout:
# 1)
# with 1st element being a connect timeout (the time it allows for the client to establish a connection to the server),
# 2) and
# the second being a read timeout (the time it will wait on a response once your client has established a connection):

get_response_timeout3 = requests.get('https://api.github.com', timeout=(0.01, 5))
# If the request:
# "establishes a connection within 2 seconds"
# ---> not then: "requests.exceptions.ConnectTimeout"
# and
# receives data within 5 seconds of the connection being established,
# ---> not then: requests.exceptions.ReadTimeout
# then the response will be returned as it was before.


from requests.exceptions import ConnectTimeout

try:
    response = requests.get('https://api.github.com', timeout=1)
except ConnectTimeout:
    print('The request timed out')
else:
    print('The request did not time out')
