from django.contrib import admin
from .models import Passenger


@admin.register(Passenger)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'gender', 'age', 'address', 'email', 'contact_number', 'source_station', 'destination_station', 'date_of_journey')
