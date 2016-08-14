"""
File that handles interfacing with iCalendar
"""
from icalendar import Calendar, Event

def make_calendar(classes):
    calendar = Calendar()
    calendar.add('prodid', '-//UNT Schedule Exporter//mxm.dk//')
    calendar.add('version', '1.0')

    for period in classes:
        event = Event()
        event.add('summary', period[0])
        event.add('dtstart', period[1])
        event.add('dtend', period[2])
        event.add('rrule', {'freq': 'weekly'})
        calendar.add_component(event)

    output = open('exported_calendar.ics', 'wb')
    output.write(calendar.to_ical())
    output.close()

if __name__ == '__main__':
    pass

