from django import forms
from .models import Volunteer

class VolunteerForm(forms.ModelForm):
    """
    Represents a volunteer.

    Attributes:
        name (str, max_length=100): The full name of the volunteer (required).
        email (str): The volunteer's email address (required).
        phone_number (str, max_length=15, blank=True): The volunteer's phone number
            (optional).

    Methods:
        __str__() (str): Returns a string representation of the volunteer object,
            typically including their name.
    """
    class Meta:
        model = Volunteer
        fields = '__all__'