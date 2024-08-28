from django.db import models
from django.contrib.auth.models import User  # Add this import

class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

class Item(models.Model):
    item_name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Disapproved', 'Disapproved')], default='Pending')
    submitted_by = models.CharField(max_length=255, blank=True, null=True)
    approved_by_principal = models.BooleanField(default=False)
    approved_by_trust = models.BooleanField(default=False)
    
    def __str__(self):
        return self.item_name

class Request(models.Model):
    REQUEST_STATUS = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Declined', 'Declined'),
    ]
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=REQUEST_STATUS, default='Pending')
    # Add other relevant fields as needed

    def __str__(self):
        return f"Request for {self.item.item_name} - {self.status}"
