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

      install_requires=["weatherbotskeleton>=1.5.3"],

      license="BSD3",

      name="randomweather_bot",
      python_requires=">=3.6",

      packages=find_packages(),

      url="https://github.com/alixnovosi/randweather_bot",

      version=VERSION)
