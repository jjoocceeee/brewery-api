from django.test import RequestFactory
from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from application.models import Brewery
import urllib

class BreweryTests(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('brewery/', include('breweries.urls')),
    ]

    def setup_data(self):
        # Testing db will be empty, so we need to setup data into it.
        Brewery.objects.create(name="Test1", state="Utah", obdb_id="test1", brewery_type="micro", city="Salt Lake")
        Brewery.objects.create(name="Test2", state="Washington", obdb_id="test2", brewery_type="large", city="Seattle")
        Brewery.objects.create(name="Test3", state="Utah", obdb_id="test3", brewery_type="micro", city="Salt Lake")
        
    def test_get_breweries(self):
        """
        Get list of breweries
        """
        self.setup_data()

        url = reverse('brewery-list')
        response = self.client.get(url, format='json')
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data.get("results")), 3)

    def test_filter_breweries(self):
        """
        Testing filtering breweries by state and city
        """
        self.setup_data()
        params = {'state': 'Washington', 'city': 'Seattle'}
        url = _build_url('brewery-list', params=params)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data.get("results")), 1)
        self.assertEqual(response.data.get("results")[0].get("city"),"Seattle")
    
    def test_get_brewery(self):
        """
        Testing getting a single brewery
        """
        self.setup_data()
        brewery = Brewery.objects.first()
        url = reverse('brewery-detail', args=[brewery.id])
        
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.get("name"), brewery.name)

def _build_url(*args, **kwargs):
    """
    Builds the URL to add params at the end.
    """
    get = kwargs.pop('params', {})
    url = reverse(*args, **kwargs)
    if get:
        url += '?' + urllib.parse.urlencode(get)
    return url