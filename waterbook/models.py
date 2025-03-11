from django.db import models
from django.contrib.auth.models import User  

class WaterBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="water_bookings")  # Each booking belongs to a user
    name = models.CharField(max_length=255)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)
    date = models.DateTimeField(auto_now_add=True)
    number_of_tins = models.PositiveIntegerField(default=1)

    PAYMENT_CASH = 'COD'
    PAYMENT_UPI = 'UPI'
    
    PAYMENT_CHOICES = [
        (PAYMENT_CASH, 'Cash on Delivery'),
        (PAYMENT_UPI, 'UPI Payment'),
    ]
    payment_method = models.CharField(max_length=3, choices=PAYMENT_CHOICES, default=PAYMENT_CASH)

    STATUS_PENDING = 'PENDING'
    STATUS_DISPATCHED = 'DISPATCHED'
    STATUS_DELIVERED = 'DELIVERED'
    
    DELIVERY_STATUS_CHOICES = [
        (STATUS_PENDING, 'Pending'),
        (STATUS_DISPATCHED, 'Dispatched'),
        (STATUS_DELIVERED, 'Delivered'),
    ]
    delivery_status = models.CharField(max_length=10, choices=DELIVERY_STATUS_CHOICES, default=STATUS_PENDING)

    def __str__(self):
        return f"Booking: {self.name} - Status: {self.get_delivery_status_display()}"
