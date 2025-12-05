# main/data.py
import time

SLOTS = [
    {"id": "S1", "label": "A1", "is_occupied": False, "last_distance": None, "last_updated": None},
    {"id": "S2", "label": "A2", "is_occupied": False, "last_distance": None, "last_updated": None},
    {"id": "S3", "label": "A3", "is_occupied": False, "last_distance": None, "last_updated": None},
]

LAST_LOG = None  # will hold the latest "serial-like" line from ESP



def get_all_slots():
    return SLOTS


def get_free_slots():
    return [slot for slot in SLOTS if not slot["is_occupied"]]


def update_slot_status(slot_id, status, distance=None, log=None):
    """Update slot, plus last distance + last log string."""
    global LAST_LOG
    for slot in SLOTS:
        if slot["id"] == slot_id:
            slot["is_occupied"] = status
            if distance is not None:
                slot["last_distance"] = distance
            slot["last_updated"] = time.strftime("%H:%M:%S")
            if log is not None:
                LAST_LOG = log
            return True

    # even if slot not found, you can still store log for debugging
    if log is not None:
        LAST_LOG = log
    return False


def get_last_log():
    return LAST_LOG
