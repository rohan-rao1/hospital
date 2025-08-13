from django.contrib import admin
from .models import Hospital, Doctor, Appointment

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    search_fields = ('name', 'address')

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'specialization', 'hospital')
    search_fields = ('name', 'specialization', 'hospital__name')

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient_name', 'doctor', 'appointment_date', 'appointment_time')
    search_fields = ('patient_name', 'doctor__name')
