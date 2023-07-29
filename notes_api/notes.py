# notes.py

from datetime import datetime


def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))


NOTES = {
    "0": {
        "title": "Tooth",
        "desc": "Fairy",
        "due_date": get_timestamp(),
    },
    "1": {
        "title": "Tooth",
        "desc": "Fairy",
        "due_date": get_timestamp(),
    },
    "2": {
        "title": "Tooth",
        "desc": "Fairy",
        "due_date": get_timestamp(),
    },
}


def read_all():
    return list(NOTES.values())
