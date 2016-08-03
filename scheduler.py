"""
Scheduler
Export UNT schedules to iCalendar format (.ics)
"""

import icalendar
from datetime import datetime

# Initialize Calendar
cal = Calendar()

# Add PRODID, VERSION
# Note: PRODID inserts "name" variable. Must be provided.
cal.add('prodid', '-//Scheduler//Schedule for ' + name + '//')
# Note: VERSION should not be changed. RFC 5545 specifies this value should remain at 2.0.
cal.add('version', '2.0')
