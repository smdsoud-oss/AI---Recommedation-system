import re

CATEGORY_KEYWORDS = {

    "earbuds": [
        "earbuds",
        "earphones",
        "airdopes",
        "tws",
        "neckband",
        "buds"
    ],

    "headphones": [
        "headphones",
        "headset"
    ],

    "speaker": [
        "speaker",
        "bluetooth speaker"
    ],

    "keyboard": [
        "keyboard",
        "mechanical keyboard",
        "wireless keyboard"
    ],

    "mouse": [
        "mouse",
        "gaming mouse",
        "wireless mouse"
    ],

    "smartwatch": [
        "watch",
        "smart watch",
        "smartwatch",
        "fitness watch"
    ],

    "charger": [
        "charger",
        "adapter",
        "fast charger"
    ],

    "pendrive": [
        "pendrive",
        "usb drive",
        "flash drive"
    ],

    "ssd": [
        "ssd",
        "solid state drive"
    ],

    "hdd": [
        "hdd",
        "hard disk"
    ],

    "webcam": [
        "webcam",
        "camera"
    ],

    "cable": [
        "cable",
        "usb cable",
        "type c cable",
        "charging cable"
    ]
}


def detect_category(query):

    query = query.lower()

    query = re.sub(r"[^a-z0-9 ]", " ", query)

    for category, keywords in CATEGORY_KEYWORDS.items():

        for keyword in keywords:

            if keyword in query:

                return category

    return None