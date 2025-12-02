# main/data.py

# This simulates our "database" for now.
# Later you can replace this with real DB queries.

SLOTS = [
    {"id": "S1", "label": "A1", "is_occupied": False},
    {"id": "S2", "label": "A2", "is_occupied": True},
    {"id": "S3", "label": "A3", "is_occupied": False},
]


def get_all_slots():
    return SLOTS


def get_free_slots():
    return [slot for slot in SLOTS if not slot["is_occupied"]]
