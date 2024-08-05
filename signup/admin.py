from django.contrib import admin
from .models import SignupAthlete

# Register your models here.
@admin.register(SignupAthlete)
class SignupAthleteAdmin(admin.AthleteAdmin):
    list_display = (
        'id', 
        'first_name',
        'last_name',
        'email',
        'emergency_contact',
        'dob',
        'headshot',
        'height',
        'weight',
        'location',
        'training_area',
        'goal',
        'injury_history',
        'preference',
        'equipment'
    )
