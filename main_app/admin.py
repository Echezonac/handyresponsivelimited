from django.contrib import admin
from .models import *

# Register your models here.
class MessageAdmin(admin.ModelAdmin):
  list_display = ['message_name','message_email','message_date']
  list_display_links = ['message_name','message_email']
  search_fields = ['message_name']
  list_filter = ['message_date']


class BookingAdmin(admin.ModelAdmin):
  list_display = ['client_name','client_email','client_message_date']
  list_display_links = ['client_name','client_email']
  search_fields = ['client_name']
  list_filter = ['client_message_date']
  
admin.site.register(Message,MessageAdmin)
admin.site.register(Booking,BookingAdmin)
admin.site.register(Hero)
admin.site.register(About)
admin.site.register(Service)
admin.site.register(Testimony)
admin.site.register(News)
admin.site.register(Contact)
admin.site.register(LocationMAp)
admin.site.register(Address)
admin.site.register(Social_Links)