"""Main class to run randomweather_bot."""

import random
import time
from os import path

import weatherbotskeleton

# Delay between tweets in seconds.
DELAY = 1800
DELAY_VARIATION = 600

if __name__ == "__main__":
    SECRETS_DIR = path.join(path.abspath(path.dirname(__file__)), "SECRETS")
    BOT_SKELETON = weatherbotskeleton.WeatherbotSkeleton(
        SECRETS_DIR,
        owner_url="https://github.com/andrewmichaud/randweather_bot",
        bot_name="randweather_bot")

    LOG = weatherbotskeleton.set_up_logging()

    while True:
        LOG.info("Sending a weather tweet.")
        weather = BOT_SKELETON.produce_status()

        LOG.info(f"Sending:\n {weather}")
        BOT_SKELETON.send(weather)

        BOT_SKELETON.set_delay(random.choice(range(DELAY-DELAY_VARIATION,
                                                   DELAY+DELAY_VARIATION+1)))
        BOT_SKELETON.nap()
