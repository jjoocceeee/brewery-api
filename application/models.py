from django.db import models

class Brewery(models.Model):
    # Not positive how all the data is, so just defaulting to varchars or length 200 :shrug:
    name = models.CharField(max_length=200)
    obdb_id = models.CharField(primary_key=True, max_length=200)
    brewery_type = models.CharField(max_length=200)
    street = models.CharField(max_length=200, blank=True, null=True)
    address_2 = models.CharField(max_length=200, blank=True, null=True)
    address_3 = models.CharField(max_length=200, blank=True, null=True)
    city = models.CharField(max_length=200, blank=True, null=True)
    state = models.CharField(max_length=200, blank=True, null=True)
    county_province = models.CharField(max_length=200, blank=True, null=True)
    postal_code = models.CharField(max_length=200, blank=True, null=True)
    website_url = models.CharField(max_length=200, blank=True, null=True)
    phone = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=200, blank=True, null=True)
    longitude = models.CharField(max_length=200, blank=True, null=True)
    latitude = models.CharField(max_length=200, blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True, null=True)
    