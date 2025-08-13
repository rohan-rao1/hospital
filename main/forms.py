from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = [
            'doctor', 
            'patient_name', 
            'patient_email', 
            'patient_phone', 
            'appointment_date', 
            'appointment_time'
        ]

        # Add Tailwind CSS classes and input types directly in widgets
        widgets = {
            'doctor': forms.HiddenInput(),  # Doctor is set in the view, no need for user to select
            'patient_name': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Your full name'
            }),
            'patient_email': forms.EmailInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Your email address'
            }),
            'patient_phone': forms.TextInput(attrs={
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Your phone number'
            }),
            'appointment_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
            'appointment_time': forms.TimeInput(attrs={
                'type': 'time',
                'class': 'w-full p-3 border border-gray-300 rounded focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
        }


