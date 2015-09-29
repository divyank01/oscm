from django.db import models
from .constants import Dropdowns


class Login(models.Model):
	userName = models.CharField(max_length=40, blank=False, null=False, primary_key=True)
	password = models.CharField(max_length=40, blank=False, null=False)
	role = roles=(('Admin',"Admin"),('SuperUser',"Super User"),('User',"User"))
	role = models.CharField(max_length=40, choices=roles, blank=False, null=False)
	lastLogin = models.DateTimeField(auto_now=False, auto_now_add=False)
	def __unicode__(self):
		return self.userName

class User(models.Model):
	userName = models.CharField(max_length=40, blank=False, null=False)
	firstName = models.CharField(max_length=40, blank=False, null=False)
	lastName = models.CharField(max_length=40, blank=False, null=False)
	email = models.EmailField()
	roles=(('admin',"Admin"),('s_user',"Super User"),('user',"User"))
	role = models.CharField(max_length=40, choices=roles, blank=False, null=False)
	def __unicode__(self):
		return self.userName

class AbuseDetails(models.Model):
	physicalAbuse = models.CharField(max_length=400, choices=Dropdowns.AbuseDetails.abusedBy, blank=False, null=False)
	oralAbuse = models.CharField(max_length=140, choices=Dropdowns.AbuseDetails.abusedBy, blank=False, null=False)
	sexualAbuse = models.CharField(max_length=140, choices=Dropdowns.AbuseDetails.abusedBy, blank=False, null=False)
	otherAbuse = models.CharField(max_length=400, blank=False, null=False)

class PersonalDetails(models.Model):
	fullName = models.CharField(max_length=400, blank=False, null=False)
	sex = models.CharField(max_length=40, choices=Dropdowns.PersonalDetails.sex, blank=False, null=False)
	ageAtAdmission = models.CharField(max_length=4, blank=False, null=False)
	currentAge = models.CharField(max_length=4, blank=False, null=False)
	religion = models.CharField(max_length=140, choices=Dropdowns.PersonalDetails.religion, blank=False, null=False)
	caseType = models.CharField(max_length=140, choices=Dropdowns.PersonalDetails.caseType, blank=False, null=False)

class ResidentialDetails(models.Model):
	residentialStatus = models.CharField(max_length=400, choices=Dropdowns.PersonalDetails.religion, blank=False, null=False)


# class MedicalDetails(models.Model):

# class ParentalDetails(models.Model)

# class Case(models.Model):
# 	abuseDetails