from django.db import models

class ParkingSlot(models.Model):
    # internal ID like S1, S2, S3
    code = models.CharField(max_length=10, unique=True)
    # human label like A1, A2, A3
    label = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.label} ({'OCCUPIED' if self.is_occupied else 'FREE'})"
