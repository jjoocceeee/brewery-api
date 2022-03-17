from application.models import Brewery
from rest_framework import serializers


class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = '__all__'

