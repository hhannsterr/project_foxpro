import json

from datetime import datetime

def get_date() -> tuple[str, str, str]:
    with open('log.json', 'r') as f:
        date = json.load(f)
    return str(date['year']), str(date['month']), str(date['day'])

def save_date() -> None:
    now = datetime.now()
    log = {
        'year': str(now.year),
        'month': str(now.month),
        'day': str(now.day)
    }
    with open('log.json', 'w') as f:
        json.dump(log, f, indent=4)
