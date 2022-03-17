from application.models import Brewery
from application.serializers import BrewerySerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


# Create your views here.
class BreweryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Breweries to be viewed or edited.
    """
    queryset = Brewery.objects.all().order_by('name')
    serializer_class = BrewerySerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'city', 'state', 'county_province', 'postal_code']