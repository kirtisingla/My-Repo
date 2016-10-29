from django.contrib import admin
from .models import Booking, Hall, Feedback

"""
All the booking details will be shown here in the table Booking.
"""
class BookingAdmin(admin.ModelAdmin):
	list_display = ['hall', 'name', 'event_name', 'date', 'start_time', 'end_time', 'email', 'status']
	class Meta:
		model = Booking

admin.site.register(Booking, BookingAdmin)

"""
Hall details will be stored in Hall table.
"""
class HallAdmin(admin.ModelAdmin):
	list_display = ['hall', 'seats', 'hall_admin']
	class Meta:
		model = Hall

admin.site.register(Hall, HallAdmin)

"""
Feedback stored will be displayed in the table Feedback.
"""
class FeedbackAdmin(admin.ModelAdmin):
	list_display = ['name', 'email', 'feedback', 'contact']
	class Meta:
model = Feedback

admin.site.register(Feedback, FeedbackAdmin)
