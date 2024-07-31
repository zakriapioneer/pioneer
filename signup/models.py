# myapp/models.py

from django.db import models

class Athlete(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)  # Ensure email is unique
    emergency_contact = models.CharField(max_length=100)  # Adjust max_length as needed
    dob = models.DateField()  # Date of birth
    headshot = models.ImageField(upload_to='headshots/')  # Stores image files in 'headshots/' directory
    height = models.FloatField()  # Use FloatField for height (you can use DecimalField if you need more precision)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
