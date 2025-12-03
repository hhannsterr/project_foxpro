import json

from datetime import datetime

def get_date() -> tuple[int]:
    with open('log.json', 'r') as f:
        date = json.load(f)
    return date['year'], date['month'], date['day']

def save_date() -> None:
    now = datetime.now()
    log = {
        'year': str(now.year),
        'month': str(now.month),
        'day': str(now.day)
    }
    with open('log.json', 'w') as f:
        json.dump(log, f, indent=4)
