from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .data import get_all_slots, get_free_slots, update_slot_status, get_last_log
from django.shortcuts import render

def dashboard(request):
    return render(request, "dashboard.html")

def all_slots_status(request):
    return JsonResponse({
        "slots": get_all_slots(),
        "debug_log": get_last_log(),
    })



def free_slots(request):
    free = get_free_slots()
    return JsonResponse({
        "count": len(free),
        "free_slots": [{"id": s["id"], "label": s["label"]} for s in free],
    })


@csrf_exempt
def update_slot(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    slot_id = data.get("id")
    status = data.get("is_occupied")
    distance = data.get("distance")
    log = data.get("log")

    if slot_id is None or status is None:
        return JsonResponse({"error": "id and is_occupied required"}, status=400)

    updated = update_slot_status(slot_id, bool(status), distance=distance, log=log)

    if updated:
        print(f"🔄 Slot {slot_id} updated: is_occupied={status}, distance={distance}")
        return JsonResponse({"message": "Status updated successfully"})
    else:
        return JsonResponse({"error": "Slot not found"}, status=404)

