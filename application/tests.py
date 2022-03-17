from django.test import TestCase

from rest_framework.test import RequestsClient

# Using the standard RequestFactory API to create a form POST request
client = RequestsClient()
response = client.get('http://testserver/brewery/')
assert response.status_code == 200