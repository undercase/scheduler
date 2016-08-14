"""
Main Execution File for Scheduler
"""

from scraper import scrape
from ical import make_calendar

if __name__ == "__main__":
    make_calendar(scrape())
