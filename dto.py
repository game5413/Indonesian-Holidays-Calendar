from dataclasses import dataclass
import datetime as dt
from const import TITLE
from icalendar import Calendar, Event
import json
from pathlib import Path

@dataclass
class DateEvent:
    date: dt.datetime
    event: str
    event_type: str

@dataclass
class IcsCalendar:
    cal: Calendar

    @classmethod
    def __init__(cls):
        cal = Calendar()
        cal.add("X-WR-CALNAME", TITLE)
        cls.cal = cal

    @classmethod
    def AddEvent(cls, evt: DateEvent) -> None:
        start = evt.date
        end = evt.date + dt.timedelta(days=1)
        _event = Event.new(
            start=start,
            end=end,
            summary=evt.event,
        )

        cls.cal.add_component(_event)
        return

    @classmethod
    def Save(cls, name: str) -> str:
        filename = f'{name}.ics'
        path = Path(filename)
        path.write_bytes(cls.cal.to_ical())
        return filename

@dataclass
class JsonCalendar:
    cal: list

    @classmethod
    def __init__(cls):
        cls.cal = []
        return

    @classmethod
    def AddEvent(cls, evt: DateEvent) -> None:
        cls.cal.append({
            'date': evt.date.strftime('%Y-%m-%d'),
            'event': evt.event,
            'type': evt.event_type,
        })
        return

    @classmethod
    def Save(cls, name: str) -> str:
        filename = f'{name}.json'

        with open(filename, 'w') as fw:
            json.dump(cls.cal, fw, indent=4)

        return filename