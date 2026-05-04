import argparse
from bs4 import BeautifulSoup
import const
from dto import DateEvent, IcsCalendar, JsonCalendar
import datetime as dt
import dateparser as dtp
import requests
from typing import List


FORMATTER = {
    const.OUTPUT_FORMAT_ICS: IcsCalendar,
    const.OUTPUT_FORMAT_JSON: JsonCalendar,
}


def get_holidays(year: int) -> List[DateEvent]:
    dates = []
    uri = const.HOLIDAY_CALENDAR_URI.format(year=year)

    page = requests.get(uri)
    soup = BeautifulSoup(page.content, 'html.parser')

    _txt = f'Daftar Hari Libur Tahun {year}'
    a = soup.find('h2', string=_txt)

    dateElems = a.parent.select('ul > li')

    for dateElem in dateElems:
        _txt_date = dateElem.select_one('div > span:last-child').text.strip()
        date = dtp.parse(f'{_txt_date} {year}', ['%d %B %Y'], ['id'])

        txt_evt = dateElem.find('span', {'aria-hidden': 'true'}).text.strip()
        txt_evt_type = dateElem.select_one('span:last-child > span:last-child').text.strip()

        dates.append(
            DateEvent(
                date=date,
                event=txt_evt,
                event_type=txt_evt_type,
            )
        )

    return dates

if __name__ == '__main__':
    arg_parser = argparse.ArgumentParser(description=f'Tools for generate ICS and JSON file for "{const.TITLE}"')
    arg_parser.add_argument('--name', type=str, required=False,
                            help='[Output file name]')
    arg_parser.add_argument('--output', type=str, required=True,
                            help='[Output format files]')

    args = arg_parser.parse_args()

    _format = args.output.split(',')

    outputs = {}

    for f in _format:
        _f = f.lower()
        if _f not in const.OUTPUT_ACCEPTED_FORMATS:
            print(f'Invalid format: {_f}')
            exit(1)
        else:
            outputs[_f] = FORMATTER[_f]()

    current_year = dt.datetime.now().year

    if args.name is not None:
        name = args.name
    else:
        name = f'{const.TITLE} {current_year}'

    events = get_holidays(current_year)
    event_total = len(events)

    for idx in range(event_total + 1):
        for output in outputs:
            if idx == event_total:
                FORMATTER[output].Save(name)
            else:
                FORMATTER[output].AddEvent(evt=events[idx])
