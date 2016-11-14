import logging

import requests


WEATHER_ROOT = "http://api.openweathermap.org/data/2.5/weather"

with open("api_key", "r") as f:
    API_KEY = f.read().strip()


OWNER_URL = "https://github.com/andrewmichaud/randomweather_bot"
USER_AGENT = "randomweather_twitterbot/1.0.0" + OWNER_URL
HEADERS = {"User-Agent": USER_AGENT}

LOG = logging.getLogger("root")


def get_zip_url(zip):
    """Format a URL to get weather by zip code from the OpenWeatherMap API."""
    return "{}?zip={},us&appid={}".format(WEATHER_ROOT, zip, API_KEY)


if __name__ == "__main__":
    url = get_zip_url(94541)
    res = requests.get(url)

    print(res.content)
