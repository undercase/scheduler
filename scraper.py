"""
Interface for web scraping
"""
import os
import sys
import getpass

from datetime import datetime

from selenium import webdriver

day_map = {
    'Mo': 'Monday',
    'Tu': 'Tuesday',
    'We': 'Wednesday',
    'Th': 'Thursday',
    'Fr': 'Friday'
}

class Class:
    def __init__(self, name, time):
        self.name = name
        self.time = time

def scrape():
    browser = webdriver.Chrome('/home/lowercase/Desktop/scheduler/chromedriver')
    browser.get('https://my.unt.edu/psp/papd01/EMPLOYEE/EMPL/h/?tab=NTPA_GUEST')
    
    euid = input('What is your EUID? ')
    password = getpass.getpass('What is your password? ')

    euid_field = browser.find_element_by_name('userid')
    password_field = browser.find_element_by_name('pwd')
    euid_field.send_keys(euid)
    password_field.send_keys(password)

    login_field = browser.find_element_by_css_selector('input[value="Login"]')
    login_field.click()

    browser.get('https://my.unt.edu/psp/papd01/EMPLOYEE/EMPL/h/?cmd=getCachedPglt&pageletname=GBPA_STUDENT_CLASSES&tab=GBPA_STUDENT&PORTALPARAM_COMPWIDTH=Narrow')

    classes = browser.find_elements_by_css_selector('p')
    return build_datetimes(parse_times(format(classes)))

def format(classes):
    formatted_classes = []
    for period in classes:
        lines = period.text.split('\n')
        name = lines[1]
        class_time = lines[2]
        formatted_classes.append(Class(name, class_time))
    return formatted_classes

def parse_times(classes):
    parsed_classes = []
    for period in classes:
        days = []
        times = []
        for term in period.time.split(' '):
            if term in ['Mo', 'Tu', 'We', 'Th', 'Fr']:
                days.append(term)
            elif term != '-':
                times.append(term)
        parsed_classes.append([days, times])
    return parsed_classes

def build_datetimes(classes):
    built_datetimes = []
    for period in classes:
        for day in period[0]:
            start_dt = datetime.strptime('%s %s' % (day_map[day], period[1][-2]), '%A %I:%M%p')
            end_dt = datetime.strptime('%s %s' % (day_map[day], period[1][-1]), '%A %I:%M%p')
            built_datetimes.append([start_dt, end_dt])
    return built_datetimes

if __name__ == "__main__":
    scrape()
