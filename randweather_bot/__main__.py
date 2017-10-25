"""Main class to run randomweather_bot."""

import os
import random
import time

import botskeleton

import weather_gen

# Delay between tweets in seconds.
DELAY = 1800
DELAY_VARIATION = 600

if __name__ == "__main__":
    SECRETS_DIR = os.path.join(os.path.abspath(os.path.dirname(__file__)), "SECRETS")
    api = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="randweather_bot")

    LOG = botskeleton.set_up_logging()

    while True:
        LOG.info("Sending a weather tweet.")
        weather = weather_gen.produce_status()
        LOG.info(f"Sending:\n {weather}")

        try:
            api.send(weather)

        except tweepy.TweepError as e:
            if e.message == "Status is a duplicate.":
                LOG.warning("Duplicate status.")
                continue

        LOG.info(f"Sleeping for {DELAY} seconds.")
        time.sleep(random.choice(range(DELAY-DELAY_VARIATION, DELAY+DELAY_VARIATION+1)))
