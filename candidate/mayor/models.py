from django.db import models

# Create your models here.
class Volunteer(models.Model):
    """
    Represents a volunteer .

    Attributes:
        name (str, max_length=100): The full name of the volunteer (required).
        email (str): The volunteer's email address (required).
        phone_number (str, max_length=15, blank=True): The volunteer's phone number
            (optional).

    Methods:
        __str__() (str): Returns a string representation of the volunteer object,
            typically including their name.
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15, blank=True)

def __str__(self):
    return self.name