# Reservamos Challenge
Project developed for the Reservamos challenge.

## How to run it?
In order to run the API you must have installed Python and Git in your system
and follow the steps in a terminal

```sh
# Get repo
> git clone https://github.com/AngelFA04/reservamos-challenge.git
> cd reservamos-challenge

# Install requirements
> pip install -r requirements.txt

# Move to application
> cd places

# Run Django server
> python manage.py runserver
```

##  How to test the API
You can run the API using any client, here is an example using cURL.
```sh
> curl "http://127.0.0.1:9000/api/forecast?city_name=CDMX"
```