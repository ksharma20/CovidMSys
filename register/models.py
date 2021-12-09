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


class CData(models.Model):
    total = models.IntegerField(default=0)
    covid = models.IntegerField(default=0)
    treatment = models.IntegerField(default=0)
    recovered = models.IntegerField(default=0)
    dead = models.IntegerField(default=0)
    discharged = models.IntegerField(default=0)

    # @staticmethod
    def total_patient(self):
        self.total += len(Patient.objects.all())
        return self.total
    
    # @staticmethod
    def add_patient(self, pid):
        patient = CovidPatient.objects.get_or_create(patient = Patient.objects.get(id=pid))
        self.covid += 1
        return patient[0].patient.name

    # @staticmethod
    def covid_patient(self):
        return self.covid

    # @staticmethod
    def under_treatment(self):
        self.treatment += len(CovidPatient.objects.all())
        return self.treatment
    
    # @staticmethod
    def add_recovered(self, cpid):
        patient = CovidPatient.objects.get(id = cpid)
        self.recovered += 1
        patient.delete()

    # @staticmethod
    def total_recovered(self):
        return self.recovered

    # @staticmethod
    def add_dead(self, cpid):
        patient = CovidPatient.objects.get(id = cpid)
        self.dead += 1
        patient.delete()

    # @staticmethod
    def total_dead(self):
        return self.dead

    # @staticmethod
    def add_discharged(self, cpid):
        patient = CovidPatient.objects.get(id = cpid)
        self.discharged += 1
        patient.delete()

    # @staticmethod
    def total_discharged(self):
        return self.discharged
