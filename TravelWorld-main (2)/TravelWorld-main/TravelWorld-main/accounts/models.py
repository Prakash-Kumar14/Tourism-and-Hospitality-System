from django.db import models


# Create your models here.
class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    check_in = models.DateField()
    check_out = models.DateField()
    room_type = models.CharField(max_length=50)
    special_requests = models.TextField(blank=True)

    def __str__(self):
        return self.name
