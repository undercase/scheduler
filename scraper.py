"""
Interface for web scraping
"""
import os
import sys

from selenium import webdriver

def scrape():
    browser = webdriver.Chrome('/home/lowercase/Desktop/scheduler/chromedriver')

if __name__ == "__main__":
    scrape()
