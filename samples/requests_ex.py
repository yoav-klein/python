

import requests

resp = requests.get('http://www.google.com')
resp.raise_for_status()