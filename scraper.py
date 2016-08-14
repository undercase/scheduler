"""
Interface for web scraping
"""
import os
import sys

import getpass

from selenium import webdriver

def scrape():
    browser = webdriver.Chrome('/home/lowercase/Desktop/scheduler/chromedriver')
    browser.get('https://my.unt.edu/psp/papd01/EMPLOYEE/EMPL/h/?tab=NTPA_GUEST')
    
    euid = input('What is your EUID?')
    password = getpass.getpass('What is your password?')

    euid_field = browser.find_element_by_name('userid')
    password_field = browser.find_element_by_name('pwd')

    euid_field.send_keys(euid)
    password_field.send_keys(password)

if __name__ == "__main__":
    scrape()
