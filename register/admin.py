from django.contrib import admin
from register.models import Patient, CovidPatient

# Register your models here.
admin.site.register(Patient)
admin.site.register(CovidPatient)