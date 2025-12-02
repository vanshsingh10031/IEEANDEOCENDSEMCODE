from django.urls import path
from .views import home
from . import views


urlpatterns = [
    path('', home, name='home'),
    path('slots/status/', views.all_slots_status, name='all_slots_status'),
    path('slots/free/', views.free_slots, name='free_slots'),
    path('slots/blink/', views.blink_slot),
]
