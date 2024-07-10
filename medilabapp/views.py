from django.shortcuts import render, redirect
from medilabapp.models import Company
from medilabapp.models import Admission
from medilabapp.models import Registration


# Create your views here.
def index(request):
    return render(request, 'index.html')


def start(request):
    return render(request, 'starter-page.html')


def about(request):
    return render(request, 'about.html')


def services(request):
    return render(request, 'services.html')


def departments(request):
    return render(request, 'departments.html')


def doctors(request):
    return render(request, 'doctors.html')


def contact(request):
    if request.method == 'POST':
        contacts = Company(name=request.POST['name'],
                           email=request.POST['email'],
                           message=request.POST['message'],
                           phone=request.POST['phone'],
                           staff=request.POST['staff'],
                           )
        contacts.save()
        return redirect('/contacts')
    else:
        return render(request, 'contact.html')


def patient(request):
    if request.method == 'POST':
        patients = Admission(name=request.POST['name'],
                             email=request.POST['email'],
                             medicalhistory=request.POST['medicalhistory'],
                             phone=request.POST['phone'],
                             age=request.POST['age'],
                             )
        patients.save()
        return redirect('/patients')
    else:
        return render(request, 'patient.html')


def appointment(request):
    if request.method == 'POST':
        appointments = Registration(name=request.POST['name'],
                                    email=request.POST['email'],
                                    phone=request.POST['phone'],
                                    date=request.POST['date'],
                                    department=request.POST['department'],
                                    doctor=request.POST['doctor'],
                                    message=request.POST['message'],
                                    )
        appointments.save()
        return redirect('/appointments')
    else:
        return render(request, 'appointment.html')


def show(request):
    data = Registration.objects.all()
    return render(request, 'show.html', {'appointments': data})


def delete(request, id):
    myappointment = Registration.objects.get(id=id)
    myappointment.delete()
    return redirect('/shows')
