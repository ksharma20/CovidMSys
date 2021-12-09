from django.shortcuts import redirect, render

from register.models import CData, Patient, CovidPatient

cdata = CData.objects.get(id=2)
# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        ptname = None

        if request.method == 'POST':
            name = request.POST.get('name')
            dob = request.POST.get('dob')
            gender = request.POST.get('gender')
            fever = request.POST.get('fever')
            cough = request.POST.get('cough')
            headache = request.POST.get('headache')
            diarrhea = request.POST.get('diarrhea')
            tasteless = request.POST.get('tasteless')
            symptoms = [True if syp!=None else False for syp in [fever, cough, headache, diarrhea, tasteless] ]
            patient = Patient.objects.create(name=name,dob=dob,gender=gender,fever=symptoms[0],cough=symptoms[1],headache=symptoms[2],diarrhea=symptoms[3],tasteless=symptoms[4])
            
            if symptoms.count(True) > 2:
                ptname = cdata.add_patient(patient.id)
        
        if ptname:
            context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all()) , 'ptname': ptname}
        else: context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all())}

        return render(request, 'dashboard.html', context)
    else: return redirect('/login')

def edit(request, id):
    if request.user.is_authenticated:
        ptname = None
        patient = Patient.objects.get(id=id)
        if request.method == 'POST':
            patient.name = request.POST.get('name')
            patient.dob = request.POST.get('dob')
            patient.gender = request.POST.get('gender')

            symptoms = [True if syp!=None else False for syp in [request.POST.get('fever'), request.POST.get('cough'), request.POST.get('headache'), request.POST.get('diarrhea'), request.POST.get('tasteless')] ]
            
            patient.fever = symptoms[0]
            patient.cough = symptoms[1]
            patient.headache = symptoms[2]
            patient.diarrhea = symptoms[3]
            patient.tasteless = symptoms[4]
            
            patient.save()
            
            if symptoms.count(True) > 2:
                ptname = cdata.add_patient(patient.id)
        
            if ptname:
                context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all()) , 'ptname': ptname}
            else: context = {'patients': reversed(Patient.objects.all()) , 'covid_patients': reversed(CovidPatient.objects.all())}
    
            return redirect('/dashboard/')

        context = {
        'patients': reversed(Patient.objects.all()), 
        'covid_patients': reversed(CovidPatient.objects.all()),
        'patient_id': patient
        }
        return render(request, 'dashboard.html', context)
    else: return redirect('/login')


def recovered(request, id):
    if request.user.is_authenticated:
        cdata.add_recovered(id)
        return redirect('/dashboard/')
    
    else: return redirect('/login')

def dead(request, id):
    if request.user.is_authenticated:
        cdata.add_dead(id)
        return redirect('/dashboard/')
    
    else: return redirect('/login')

def discharged(request, id):
    if request.user.is_authenticated:
        cdata.add_discharged(id)
        return redirect('/dashboard/')
    
    else: return redirect('/login')

