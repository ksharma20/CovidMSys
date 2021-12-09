from django.shortcuts import redirect, render
from home.models import CData
from register.models import Patient, CovidPatient


# Create your views here.
def dashboard(request):
    cdata = CData.objects.get(id=1)
    if request.user.is_authenticated:
        ptname = None

        if request.method == 'POST':
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            fever = bool(request.POST.get('fever'))
            cough = bool(request.POST.get('cough'))
            headache = bool(request.POST.get('headache'))
            diarrhea = bool(request.POST.get('diarrhea'))
            tasteless = bool(request.POST.get('tasteless'))
            symptoms = [fever, cough, headache, diarrhea, tasteless]
            patient = Patient.objects.create(name=name,dob=dob,gender=gender,fever=symptoms[0],cough=symptoms[1],headache=symptoms[2],diarrhea=symptoms[3],tasteless=symptoms[4])
            
            if symptoms.count(True) > 2:
                ptname, created = CovidPatient.objects.get_or_create(patient=patient)
                if created:
                    cdata.covid += 1
                    cdata.save()
        
        if ptname:
            context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all()) , 'ptname': ptname.patient.name}
        else: context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all())}

        return render(request, 'dashboard.html', context)
    else: return redirect('/login')

def edit(request, id):
    cdata = CData.objects.get(id=1)
    if request.user.is_authenticated:
        ptname = None
        patient = Patient.objects.get(id=id)
        if request.method == 'POST':
            patient.name = request.POST.get('name')
            patient.gender = request.POST.get('gender')

            symptoms = [bool(request.POST.get('fever')), bool(request.POST.get('cough')), bool(request.POST.get('headache')), bool(request.POST.get('diarrhea')), bool(request.POST.get('tasteless'))]
            
            patient.fever = symptoms[0]
            patient.cough = symptoms[1]
            patient.headache = symptoms[2]
            patient.diarrhea = symptoms[3]
            patient.tasteless = symptoms[4]
            
            patient.save()
            
            if symptoms.count(True) > 2:
                ptname, created = CovidPatient.objects.get_or_create(patient=patient)
                if created:
                    cdata.covid += 1
                    cdata.save()
        
            if ptname:
                context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all()) , 'ptname': ptname.patient.name}
            else: context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all())}
    
            return redirect('/dashboard/')
        print('Patient Gender: ',patient.gender)
        context = {
        'patients': reversed(Patient.objects.all()), 
        'covid_patients': reversed(CovidPatient.objects.all()),
        'patient_id': patient
        }
        return render(request, 'dashboard.html', context)
    else: return redirect('/login')


def recovered(request, id):
    cdata = CData.objects.get(id=1)
    if request.user.is_authenticated:
        cdata.recovered += 1
        cdata.save()
        CovidPatient.objects.get(id=id).delete()
        return redirect('/dashboard/')
    
    else: return redirect('/login')

def dead(request, id):
    cdata = CData.objects.get(id=1)
    if request.user.is_authenticated:
        cdata.dead += 1
        cdata.save()
        CovidPatient.objects.get(id=id).delete()
        return redirect('/dashboard/')
    
    else: return redirect('/login')

def discharged(request, id):
    cdata = CData.objects.get(id=1)
    if request.user.is_authenticated:
        cdata.discharged += 1
        cdata.save()
        CovidPatient.objects.get(id=id).delete()
        return redirect('/dashboard/')
    
    else: return redirect('/login')

