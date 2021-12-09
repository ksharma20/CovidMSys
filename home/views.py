from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from home.models import CData
from register.models import Patient, CovidPatient

# Create your views here.
def home(request):
    cdata = CData.objects.get(id=1)
    cdata.total = len(Patient.objects.all())
    cdata.treatment = len(CovidPatient.objects.all())
    cdata.save()
    context = {
        'btname': 'Login',
        'btna': '/login', 
        'total_patents': cdata.total, 
        'covid_patents': cdata.covid,
        'under_treatment': cdata.treatment,
        'total_recovered': cdata.recovered,
        'total_dead': cdata.dead,
        'total_discharged': cdata.discharged,
        }

    if request.user.is_authenticated:
        context['btname'] = 'Dashboard'
        context['btna'] = '/dashboard'
        return render(request, 'home.html', context)
    else:
        return render(request, 'home.html', context)

def ulogin(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        passwd = request.POST.get('passwd')
        user = authenticate(username=uname, password=passwd)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')

    if request.user.is_authenticated:
        logout(request)
        return redirect('/')
    else:
        return render(request, 'login.html')