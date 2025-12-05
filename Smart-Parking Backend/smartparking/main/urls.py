# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),

    # status APIs
    path("slots/status/", views.all_slots_status, name="all_slots_status"),
    path("slots/free/", views.free_slots, name="free_slots"),
    path("slots/update/", views.update_slot, name="update_slot"),

    # find-my-car APIs
    path("slots/find/", views.find_my_car, name="find_my_car"),
    path("slots/find/stop/", views.find_my_car_stop, name="find_my_car_stop"),
    path("slots/find/state/", views.find_state, name="find_state"),
]
