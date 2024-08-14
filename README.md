# Reservamos Challenge
Project developed for the Reservamos challenge.

## How to run it?
In order to run the API you must have installed Python and Git in your system
and follow the steps in a terminal. Its important that you run it in a UNIX enviroment.

### Install the dependences
```sh
# Get repo
> git clone https://github.com/AngelFA04/reservamos-challenge.git
> cd reservamos-challenge

# Install requirements
> pip install -r requirements.txt
```
### Run the server


```sh
# Move to application
> cd places

# Initialize the Openweather API Key variable
> export OPENWEATHER_API_KEY=<your-api-key>
# Run Django server
> python manage.py runserver 9000
```

##  How to test the API
You can run the API using any client, here is an example using cURL.
```sh
> curl "http://127.0.0.1:9000/api/forecast?city_name=CDMX"
```