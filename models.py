rom django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime


"""
It contains the informations of the current booking status of various halls it should have unique hall and date and 
time values. If the hall is already booked its booking_status will be True, otherwise False.
"""
class Booking(models.Model):
	hall = models.ForeignKey('Hall')
	date = models.DateField(auto_now=False, auto_now_add=False)
	start_time = models.TimeField(auto_now=False, auto_now_add=False)
	end_time = models.TimeField(auto_now=False, auto_now_add=False)
	# duration = models.PositiveSmallIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
	name = models.CharField(max_length=30)
	email = models.EmailField('Email', max_length=30)
	event_name = models.CharField(max_length=30)
	status = models.BooleanField(default=False)
	# cancel = models.BooleanField(default=False)
	
	class Meta:
    		unique_together = ('hall', 'date', 'start_time',)
	
	def __unicode__(self):
		return '%s' % (self.event_name)

"""
It contains the information about the Hall, i.e. what is the name of the hall and its other hall featured related 
informations.
"""
class Hall(models.Model):
	hall = models.CharField(max_length=25, unique=True)
	seats = models.PositiveSmallIntegerField()
	hall_admin = models.EmailField(max_length=40)

	class Meta:
		unique_together = ('hall', 'hall_admin')
	
	def __unicode__(self):
		return '%s' % (self.hall)
"""
This model stores the feedback from the anonymous user and stores it in the database.
"""
class Feedback(models.Model):
	name = models.CharField(max_length=30)
email = models.EmailField('Email', max_length=30)
	contact = models.CharField(max_length=10)
	feedback = models.TextField()

	def __unicode__(self):
return '%s' % (self.name)
