"""Main class to run randomweather_bot."""

import random
import time
from os import path

import botskeleton

import weather_gen

# Delay between tweets in seconds.
DELAY = 1800
DELAY_VARIATION = 600

if __name__ == "__main__":
    SECRETS_DIR = path.join(path.abspath(path.dirname(__file__)), "SECRETS")
    api = botskeleton.BotSkeleton(SECRETS_DIR, bot_name="randweather_bot")

    LOG = botskeleton.set_up_logging()

    while True:
        LOG.info("Sending a weather tweet.")
        try:
            weather = weather_gen.produce_status()
        except Exception as e:
            api.send_dm_sos(f"Bot {api.bot_name} had an error it can't recover from!\n{e}")
            raise

        LOG.info(f"Sending:\n {weather}")

        try:
            api.send(weather)

        except tweepy.TweepError as e:
            if e.message == "Status is a duplicate.":
                LOG.warning("Duplicate status.")
                continue
            else:
                api.send_dm_sos(f"Bot {api.bot_name} had an error it can't recover from!\n{e}")
                raise

        FINAL_DELAY = random.choice(range(DELAY-DELAY_VARIATION, DELAY+DELAY_VARIATION+1))
        LOG.info(f"Sleeping for {FINAL_DELAY} seconds.")
        time.sleep(FINAL_DELAY)
