from django.db import models

# Create your models here.
class Patient(models.Model):

    name = models.CharField(max_length=100, default='')
    dob = models.DateField()
    gender = models.CharField(max_length=7, choices=[('Male', 'Male'),('Female', 'Female')], default='Male')
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    headache = models.BooleanField(default=False)
    diarrhea = models.BooleanField(default=False)
    tasteless = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class CovidPatient(models.Model):
    
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
 
    def __str__(self):
        return self.patient.name
