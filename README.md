# scheduler
Export UNT schedules to iCalendar.

## Installation
### Requirements
Python 3 is needed. Dependencies will be installed through pip. It is highly recommended you use a virtualenv.

### Procedure
0. (Highly recommended) Create a virtualenv (`$ virtualenv venv`) and then `$ source venv/bin/activate`.
1. Install dependencies through `$ pip3 install -r requirements.txt`.
2. Run with `$ python3 main.py`. If you see a browser window open, **don't disrupt it**. Instead, enter your EUID and password through the terminal. Your information will be securely routed to that browser window so the script can retrieve your schedule through myUNT.

### Troubleshooting
Selenium has a bug that breaks scheduler on OS X, but here's how to fix it in case you encounter it. If an error like this appears:
```
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    from scraper import scrape
  File "/path/to/scheduler/scraper.py", line 13, in <module>
    from selenium import webdriver
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/__init__.py", line 25, in <module>
    from .safari.webdriver import WebDriver as Safari  # noqa
  File "/usr/local/lib/python3.5/site-packages/selenium/webdriver/safari/webdriver.py", line 49
    executable_path = os.environ.get("SELENIUM_SERVER_JAR")
                                                          ^
TabError: inconsistent use of tabs and spaces in indentation
```
you will need to edit the file `/usr/local/lib/python3.5/site-packages/selenium/webdriver/safari/webdriver.py`, go to line 49, and change the tab at the very front of the line containing `executable_path = os.environ.get("SELENIUM_SERVER_JAR")` into 4 spaces.

## Development
Scheduler was written by Thomas Hobohm (@undercase) with assistance provided by Jeffrey Wang (@jeffw16) and Garrett Gu (@garrettgu10).

### Organization
Scheduler is divided into three Python files:

1. *main.py* - Contains main execution code to interface between webdriver and iCalendar.

2. *scraper.py* - Contains a class to facilitate scraping the UNT website for scheduling information.

3. *ical.py* - Interfaces with iCalendar to build a .ics file.

There are three working branches:

1. *master* - Contains current version of application.

2. *scraping* - Used to make revisions to web scraping code / interface.

3. *calendar* - Used to make revisions to iCalendar integration code.
