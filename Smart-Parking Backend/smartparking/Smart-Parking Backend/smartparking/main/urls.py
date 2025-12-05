from django.urls import path
from . import views


urlpatterns = [
    path('slots/status/', views.all_slots_status, name='all_slots_status'),
    path('slots/free/', views.free_slots, name='free_slots'),
    path('slots/update/', views.update_slot),
]
