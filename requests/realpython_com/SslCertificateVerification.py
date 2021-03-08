import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

# Certyfikat SSL

# Certyfikat SSL to narzędzie poświadczające wiarygodność domeny bądź domeny oraz jej właściciela.
# Potwierdza bezpieczeństwo szyfrowania danych przesyłanych pomiędzy użytkownikiem a serwerem.
# Jest gwarantem zachowania poufności danych i całej komunikacji. Gwarancja ta jest udzielana przez niezależny podmiot czyli wystawcę.

# Do szyfrowania danych wykorzystuje się certyfikat o określonej długości klucza.
# Im klucz certyfikatu jest dłuższy, tym trudniej jest odszyfrować przesyłane dane. Obecnie dostępne są certyfikaty 128 lub 256 bit.



# Po czym poznać, że strona jest zabezpieczona certyfikatem?
# Kiedy stosować certyfikat SSL?
# Jakie są rodzaje certyfikatów SSL?



# "SSL Certificate Verification"

# Any time the data you are trying to send or receive is sensitive, security is important.

# The way that you communicate with secure sites over HTTP is by
# --> establishing an encrypted connection using SSL,
# --> which means that verifying the target server’s SSL Certificate is critical.


# The good news is that requests does this for you by default.
# However, there are some cases where you might want to change this behavior.


# If you want to disable SSL Certificate verification, you pass False to the verify parameter of the request function

try:
    nossl_get_response = requests.get('https://api.github.com', verify=False)
except InsecureRequestWarning as e:
    print(e)
# InsecureRequestWarning

print(nossl_get_response.status_code)



# SSL Cert Verification
# https://requests.readthedocs.io/en/latest/user/advanced/

# requests.get('https://github.com', verify='/path/to/certfile')
# Client Side Certificates
# requests.get('https://kennethreitz.org', cert=('/path/client.cert', '/path/client.key'))

# Note: requests uses a package called certifi to provide Certificate Authorities.
