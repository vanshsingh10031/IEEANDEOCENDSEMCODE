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


# 🔎 FIND MY CAR helpers

def set_find_slot(slot_id):
    """Set exactly one slot as the 'find my car' slot."""
    found = False
    for slot in SLOTS:
        if slot["id"] == slot_id:
            slot["find_my_car"] = True
            found = True
        else:
            slot["find_my_car"] = False
    return found
# main/data.py
import time

# In-memory slots
SLOTS = [
    {"id": "S1", "label": "A1", "is_occupied": False, "last_distance": None, "last_updated": None},
    {"id": "S2", "label": "A2", "is_occupied": False, "last_distance": None, "last_updated": None},
    {"id": "S3", "label": "A3", "is_occupied": False, "last_distance": None, "last_updated": None},
]

LAST_LOG = None          # last serial-like log line from ESP
FIND_TARGET_ID = None    # S1 / S2 / S3 or None


def get_all_slots():
    """Return slots; 'find_my_car' will be attached in the view using FIND_TARGET_ID."""
    return SLOTS


def get_free_slots():
    return [slot for slot in SLOTS if not slot["is_occupied"]]


def update_slot_status(slot_id, status, distance=None, log=None):
    """Update slot occupancy + distance + last log."""
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

    # If unknown slot, still store log for debugging
    if log is not None:
        LAST_LOG = log
    return False


def get_last_log():
    return LAST_LOG


# ---------- Find-my-car helpers ----------

def set_find_target(slot_id):
    """Set which slot should blink (S1/S2/S3)."""
    global FIND_TARGET_ID
    FIND_TARGET_ID = slot_id


def clear_find_target():
    """Stop blinking on all slots."""
    global FIND_TARGET_ID
    FIND_TARGET_ID = None


def get_find_target():
    """Return current target slot id or None."""
    return FIND_TARGET_ID


def clear_find_slot():
    for slot in SLOTS:
        slot["find_my_car"] = False


def get_find_slot_id():
    for slot in SLOTS:
        if slot.get("find_my_car"):
            return slot["id"]
    return None