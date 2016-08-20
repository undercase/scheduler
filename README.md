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
Selenium WebDriver's Python package has a bug that breaks Scheduler on OS X. If an error like this appears:
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
you will need to edit the file `/usr/local/lib/python3.5/site-packages/selenium/webdriver/safari/webdriver.py`; go to line 49 and change the tab at the very front of the line containing `executable_path = os.environ.get("SELENIUM_SERVER_JAR")` into 4 spaces.

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

## Disclaimer
Scheduler accesses the myUNT service via your computer. The program is only automating the gathering of your schedule data. Absolutely no data is transmitted to the developers or any other third party at any time whatsoever. There is only an internet connection between UNT and you.

The [server version of Scheduler](https://github.com/undercase/scheduler-server) is officially running at https://www.schedulerapp.net; it's currently located on a secure remote server and connections are securely transmitted over encrypted SSL. The developers of Scheduler have implemented this service solely for the benefit of the general public. UNT strongly advises you to keep your EUID password secure and away from third parties. The safest way for you to do so is to use the client version of Scheduler, which is just as safe as going to myUNT from your computer and accessing your schedule. The second safest way is to use the [online version of Scheduler](https://www.schedulerapp.net) and change your password immediately after on [AMS](https://ams.unt.edu).
