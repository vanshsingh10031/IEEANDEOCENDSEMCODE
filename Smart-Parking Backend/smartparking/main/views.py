# main/views.py
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .data import (
    get_all_slots,
    get_free_slots,
    update_slot_status,
    get_last_log,
    set_find_target,
    clear_find_target,
    get_find_target,
)


def dashboard(request):
    return render(request, "dashboard.html")


def all_slots_status(request):
    """Return current status of all slots + which one is in find-my-car mode."""
    slots = get_all_slots()
    find_id = get_find_target()

    data = [
        {
            "id": slot["id"],
            "label": slot["label"],
            "is_occupied": slot["is_occupied"],
            "last_distance": slot.get("last_distance"),
            "last_updated": slot.get("last_updated"),
            "find_my_car": (slot["id"] == find_id),
        }
        for slot in slots
    ]

    return JsonResponse(
        {
            "slots": data,
            "debug_log": get_last_log(),
        }
    )


def free_slots(request):
    slots = get_free_slots()
    return JsonResponse({"free_slots": [s["id"] for s in slots]})


@csrf_exempt
def update_slot(request):
    """Called by ESP32 to update occupancy + distance + log."""
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    try:
        body = request.body.decode("utf-8")
        data = json.loads(body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    slot_id = data.get("id")
    is_occupied = data.get("is_occupied")
    distance = data.get("distance")
    log = data.get("log")

    if slot_id is None or is_occupied is None:
        return JsonResponse({"error": "id and is_occupied are required"}, status=400)

    ok = update_slot_status(slot_id, bool(is_occupied), distance=distance, log=log)

    return JsonResponse({"success": ok})
    

# ---------- Find-my-car endpoints ----------

@csrf_exempt
def find_my_car(request):
    """
    POST /api/slots/find/
    Body: {"id": "S1"}   -> mark S1 as the slot to blink
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    try:
        body = request.body.decode("utf-8")
        data = json.loads(body or "{}")
    except json.JSONDecodeError:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    slot_id = data.get("id")

    if not slot_id:
        return JsonResponse({"error": "id is required, e.g. 'S1'"}, status=400)

    # (optional) validate slot id exists
    slot_ids = [s["id"] for s in get_all_slots()]
    if slot_id not in slot_ids:
        return JsonResponse({"error": f"Unknown slot id {slot_id}"}, status=400)

    set_find_target(slot_id)
    return JsonResponse({"message": f"Find-my-car set to {slot_id}"})


@csrf_exempt
def find_my_car_stop(request):
    """
    POST /api/slots/find/stop/
    Clears the find-my-car target.
    """
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=400)

    clear_find_target()
    return JsonResponse({"message": "Find-my-car cleared"})


def find_state(request):
    """
    GET /api/slots/find/state/
    Response: {"id": "S1"} or {"id": null}
    Used by ESP32.
    """
    return JsonResponse({"id": get_find_target()})
