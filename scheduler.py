"""
Scheduler
Export UNT schedules to iCalendar format (.ics)
"""

import icalendar
from datetime import datetime

if __name__ == "__main__":
    cal = Calendar()
    cal.add('prodid', '-//Scheduler//Schedule for ' + name + '//')
    # VERSION should not be changed - must remail at 2.0
    cal.add('version', '2.0')
