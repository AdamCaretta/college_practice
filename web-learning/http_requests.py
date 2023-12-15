import requests

"""
x = requests.get('https://www.graderthan.com')
print(x.status_code)
print(x.text)
"""

x = requests.post("https://www.graderthan.com", {"key": "value"})
print(x.status_code)
print(x.text)
