from django.http import HttpResponse, JsonResponse
from .data import get_all_slots, get_free_slots
import json
from django.views.decorators.csrf import csrf_exempt


def home(request):
    return HttpResponse("Hello, Django! 🚀")

def all_slots_status(request):
    slots = get_all_slots()
    data = {
        "slots": slots
    }
    return JsonResponse(data)


def free_slots(request):
    free = get_free_slots()
    data = {
        "count": len(free),
        "free_slots": [
            {"id": slot["id"], "label": slot["label"]}
            for slot in free
        ],
    }
    return JsonResponse(data)


@csrf_exempt
def blink_slot(request):
    if request.method != "POST":
        return JsonResponse({"error": "POST request required"}, status=400)

    try:
        data = json.loads(request.body.decode("utf-8"))
    except:
        return JsonResponse({"error": "Invalid JSON"}, status=400)

    slot_id = data.get("id")

    if not slot_id:
        return JsonResponse({"error": "id required"}, status=400)

    print(f"🚗 Blink request received for slot: {slot_id}")  # Debug log for testing

    # Pseudo action: Pretend we blink the light
    return JsonResponse({"message": f"Blink triggered for {slot_id}"})