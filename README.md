# Brewery API 
This is a basic Django Rest Application meant to display and filter breweries from 
a database containing brewery data (https://www.openbrewerydb.org/documentation). I stood up a AWS RDS postgres db for this demo, which you can connect to.


## Getting Started
### Setup
- Clone repo
- Install dependencies
  `pip install requirements.txt`
- Connect to Database (steps below)
- run django server
  `python ./manage.py runserver`


### Connecting to DB
This is a basic Django application for an Breweries. It will work with a Database implementation of breweries DB (https://www.openbrewerydb.org/documentation).


#### Adding DB Information
In `breweries/settings.py` you will need to add the Database information with the correct data filled out:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'HOST': '',
        'USER': '',
        'PASSWORD': '',
    }
}
```

### Postman Collection
To quickly test via Postman, import the Brewery Postman collection found in `Brewery.postman_collection.json`


### Running Tests
The test runner can be found in `runtests.py`. 
To run tests use the following command
```
python ./manage.py test
```


#### Tools used
- Basic python + Django scafolding tools.
- gitignore.io
