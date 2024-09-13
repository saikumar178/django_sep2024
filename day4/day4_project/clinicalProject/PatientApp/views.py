from django.shortcuts import render
from django.shortcuts import redirect
# Create your views here.
from .models import Patient

# List all patients
def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

# Create a new patient
def patient_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        disease = request.POST['disease']
        age = request.POST['age']
        Patient.objects.create(name=name, disease=disease, age=age)
        return redirect('patient_list')
    return render(request, 'patient_form.html')

# Update an existing patient
def patient_update(request, id):
    patient = Patient.objects.get(id=id)
    if request.method == 'POST':
        patient.name = request.POST['name']
        patient.disease = request.POST['disease']
        patient.age = request.POST['age']
        patient.save()
        return redirect('patient_list')
    return render(request, 'patient_form.html', {'patient': Patient})

# Delete a patient
def patient_delete(request, id):
    patient = Patient.objects.get(id=id)
    patient.delete()
    return redirect('patient_list')