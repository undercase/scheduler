# scheduler
Export UNT schedules to iCalendar.

## Installation
### Requirements
Python 3 is needed. Dependencies will be installed through pip. It is highly recommended you use a virtualenv.

### Procedure
0. (Highly recommended) Create a virtualenv (`$ virtualenv venv`) and then `$ source venv/bin/activate`.
1. Install dependencies through `$ pip3 install -r requirements.txt`.
2. Run with `$ python3 main.py`. If you see a browser window open, **don't disrupt it**. Instead, enter your EUID and password through the terminal. Your information will be securely routed to that browser window so the script can retrieve your schedule through myUNT.

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
