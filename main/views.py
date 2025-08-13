from django.shortcuts import render, redirect
from .models import Hospital, Doctor
from .forms import AppointmentForm
from django.db.models import Q
from django.core.mail import send_mail

def index(request):
    query = request.GET.get('q', '')
    if query:
        hospitals = Hospital.objects.filter(
            Q(name__icontains=query) | Q(address__icontains=query) | Q(doctors__name__icontains=query)
        ).distinct().prefetch_related('doctors')
    else:
        hospitals = Hospital.objects.all().prefetch_related('doctors')
    return render(request, 'main/index.html', {'hospitals': hospitals, 'query': query})

def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.doctor = doctor
            appointment.save()

            # Email to patient
            send_mail(
                subject=f'Appointment Confirmation with {doctor.name}',
                message=f"Hi {appointment.patient_name},\n\nYour appointment with Dr. {doctor.name} ({doctor.specialization}) at {doctor.hospital.name} is confirmed on {appointment.appointment_date} at {appointment.appointment_time}.",
                from_email=None,
                recipient_list=[appointment.patient_email],
                fail_silently=False
            )

            # Email to doctor
            if doctor.email:
                send_mail(
                    subject=f'New Appointment with {appointment.patient_name}',
                    message=f"Hi Dr. {doctor.name},\n\nYou have a new appointment with {appointment.patient_name} on {appointment.appointment_date} at {appointment.appointment_time}.",
                    from_email=None,
                    recipient_list=[doctor.email],
                    fail_silently=False
                )

            return redirect('index')
    else:
        form = AppointmentForm(initial={'doctor': doctor})
    return render(request, 'main/book_appointment.html', {'form': form, 'doctor': doctor})

