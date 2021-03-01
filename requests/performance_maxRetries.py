

# Max Retries

# If a request fails, you may want your app to retry the same request. However, requests will not do this for u by def.
#
# To apply this functionality, you need to implement a custom Transport Adapter.
# https://2.python-requests.org/en/master/user/advanced/#transport-adapters


# Transport Adapters let you define a set of configurations per service you’re interacting with.

# For example
# lets say you want all requests to https://api.github.com to retry three times before finally raising a ConnectionError

# You would build a Transport Adapter, set its max_retries parameter, and mount it to an existing Session:

import requests
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError

github_adapter = HTTPAdapter(max_retries=3)

session = requests.Session()

# Use 'github_adapter' for all requests to endpoints that start with this URL
session.mount('https://api.github.com', github_adapter)

try:
    session.get('https://api.github.com')
except ConnectionError as ce:
    print(ce)

# When you mount "the HTTPAdapter, github_adapter, to session",
# session will adhere to its configuration for each request to https://api.github.com.

# Timeouts, Transport Adapters, and sessions are for keeping your code efficient and your application resilient.
