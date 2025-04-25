from django import forms
from .models import Passenger


class PassengerRegistration(forms.ModelForm):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.RadioSelect)

    class Meta:
        model = Passenger
        fields = ['id', 'full_name', 'gender', 'age', 'address', 'email', 'contact_number', 'source_station',
                  'destination_station', 'date_of_journey']
        labels = {
            'full_name': 'Enter Full Name', 'gender': 'Enter Gender', 'age': 'Enter Age',
            'address': 'Enter Address', 'email': 'Enter Email', 'contact_number': 'Enter Contact Number',
            'source_station': 'Enter Source Station', 'destination_station': 'Enter Destination Station',
            'date_of_journey': 'Select Date of Journey'
        }
        widgets = {'date_of_journey': forms.DateInput(attrs={'type': 'date'})}
