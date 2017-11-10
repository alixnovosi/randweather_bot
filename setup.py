from os import path
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, "VERSION"), encoding="utf-8") as f:
    VERSION = f.read().strip()

setup(author="Andrew Michaud",
      author_email="bots+randomweather@mail.andrewmichaud.com",

      entry_points={
          "console_scripts": ["randomweather_bot = randomweather_bot.__main__:main"]
      },

      install_requires=["botskeleton>=1.1.0", "requests>=2.11.1"],

      license="BSD3",

      name="randomweather_bot",
      requires="python>=3.6.0".

      packages=find_packages(),

      # Project"s main homepage
      url="https://github.com/andrewmichaud/randweather_bot",

      version=VERSION)
