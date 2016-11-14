import datetime
import logging
import random
from enum import Enum

import requests

import util


WEATHER_ROOT = "http://api.openweathermap.org/data/2.5/weather"

with open("api_key", "r") as f:
    API_KEY = f.read().strip()


OWNER_URL = "https://github.com/andrewmichaud/randweather_bot"
USER_AGENT = "randweather_twitterbot/1.0.0" + OWNER_URL
HEADERS = {"User-Agent": USER_AGENT}

LOG = logging.getLogger("root")


def produce_status():
    """Produce status from the current weather somewhere."""
    json = get_weather_from_api()
    LOG.debug("Full JSON from weather API: {}".format(json))

    place_name = json["name"]
    LOG.info("Producing weather status for {}".format(place_name))

    thing = random.choice(list(WeatherThings))

    if thing == WeatherThings.WIND_SPEED:
        LOG.info("Producing a status on wind speed.")
        wind_speed = json["wind"]["speed"]

        return "The {} in {} is {} {}.".format("current wind speed", place_name, wind_speed,
                                               "meters/second")
    elif thing == WeatherThings.CLOUDINESS:
        LOG.info("Producing a status on cloudiness.")
        cloudiness = json["clouds"]["all"]

        return "It is {}% cloudy in {}.".format(cloudiness, place_name)

    elif thing == WeatherThings.SUNRISE or thing == WeatherThings.SUNSET:
        LOG.info("Producing a status on the sunrise.")

        if thing == WeatherThings.SUNRISE:
            LOG.info("Producing a status on the sunrise.")
            sunthing_time = json["sys"]["sunrise"]
            sunthing = "sunrise"

        else:
            LOG.info("Producing a status on the sunset.")
            sunthing_time = json["sys"]["sunset"]
            sunthing = "sunset"

        sunthing_datetime = datetime.datetime.utcfromtimestamp(int(sunthing_time))
        formatted_datetime = sunthing_datetime.strftime("%H:%M:%S")

        now = datetime.datetime.utcnow()

        if now > sunthing_datetime:
            return "The last {} in {} happened at {} UTC.".format(sunthing, place_name,
                                                                  formatted_datetime)

        elif now == sunthing_datetime:
            return "The {} is happening now in {}.".format(sunthing, place_name)

        else:
            return "The next {} in {} will happen at {} UTC.".format(sunthing, place_name,
                                                                     formatted_datetime)

    elif thing == WeatherThings.HUMIDITY:
        LOG.info("Producing a status on humidity.")
        humidity = json["main"]["humidity"]

        if random.choice(range(2)) > 0:
            return "The humidity in {} is {}%, currently.".format(place_name, humidity)

        else:
            return "It is {}% humid in {} right now.".format(humidity, place_name)

    elif thing == WeatherThings.TEMP:
        LOG.info("Producing a status on temperature.")
        temp = json["main"]["temp"]

        if random.choice(range(2)) > 0:
            celsius_temp = round(float(temp) - 273.15, 2)
            return "It's {} degrees Celsius in {} right now.".format(celsius_temp, place_name)

        else:
            fahrenheit_temp = round((float(temp) * (9.0 / 5)) - 459.67, 2)
            return "It's {} degrees Fahrenheit in {} right now.".format(fahrenheit_temp,
                                                                        place_name)


def get_weather_from_api():
    """Get weather blob for a random city from the openweathermap API."""
    zip = util.random_line("ZIP_CODES")
    LOG.info("Random zip code is {}.".format(zip))
    url = get_zip_url(zip)

    weather = openweathermap_api_call(url)

    return weather.json()


def get_zip_url(zip):
    """Format a URL to get weather by zip code from the OpenWeatherMap API."""
    return "{}?zip={},us&appid={}".format(WEATHER_ROOT, zip, API_KEY)


@util.rate_limited(10)
def openweathermap_api_call(url):
    """Perform a rate-limited API call."""
    return requests.get(url)


class WeatherThings(Enum):
    """Kinds of weather we can pull out of a weather blob from the OWM API."""
    WIND_SPEED = 000
    CLOUDINESS = 100
    SUNRISE = 200
    SUNSET = 300
    HUMIDITY = 400
    TEMP = 500
