from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from register.models import CData

# Create your views here.
def home(request):
    cd = CData.objects.get(id=2)
    context = {
        'btname': 'Login', 
        'btna': '/login', 
        'total_patents': cd.total_patient(), 
        'covid_patents': cd.covid_patient(),
        'under_treatment': cd.under_treatment(),
        'total_recovered': cd.total_recovered(),
        'total_dead': cd.total_dead(),
        'total_discharged': cd.total_discharged(),
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