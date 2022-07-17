from setuptools import setup
VERSION = "0.0.1"
DESCRIPTION = "Just sev stats scraper"
LONG_DESCRIPTION = "A packge to scrape stats from TheBigBoss.org."


setup(
    name="tbbScraper",
    version=VERSION,
    author="ExTBH",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=['tbbScraper'],
    install_requires=['requests', 'bs4'],
    python_requires=">=3.8"
)