from django.core.exceptions import ValidationError
from django.db.models import Q
from django import forms
from .models import Booking
from datetime import timedelta
import datetime


"""
This form is used for booking the hall for an event by registered users and the request will be sent to the admin only
if the timing slot is available for booking.
"""
class BookingForm(forms.ModelForm):
	# This connects the 'Booking' model with this form and shows the specified fields on the html.
	class Meta:
		model = Booking 
		exclude = ['status', 'email']

	"""
	If the input date is not valid then it will show a validation message.
	The form will also raise a validation error if the start time or the end time of the event is between the timings 
	for	already booked or hall to be booked. e.g. If the hall is booked from 8AM to 10AM, then the user can't book 
	the hall from 9AM to 10AM.
	"""
	def clean(self):
		try:	
			# Getting form data used for checking whether the booking can be done or not for filled entries.
			form_data = self.cleaned_data
			event_date = form_data['date']
			event_hall = form_data['hall']
			event_start = form_data['start_time']
			event_end = form_data['end_time']
			
			# Getting the current date and time for comparing
time_now = datetime.datetime.now().strftime('%H:%M:00')
			date_today = datetime.date.today()

			# For converting event_start from datetime.time to datetime.datetime, combine method is used for it and then 
			# adding or subtracting number of hours from it.
			e_start = (datetime.datetime.combine(datetime.date.today(), event_start) + datetime.timedelta(minutes = 1))\
			.strftime('%H:%M:00')
			e_end = (datetime.datetime.combine(datetime.date.today(), event_end) - datetime.timedelta(minutes = 1)).\
			strftime('%H:%M:00')

			# For checking if the start_time is less than end_time such that timing should be valid.
			if (event_start >= event_end):
				raise forms.ValidationError("Invalid Timings")
