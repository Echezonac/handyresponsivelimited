from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import *

# Create a message form 
class MessageForm(ModelForm):
  class Meta:
    model = Message
    fields = "__all__"
    
    widgets = {
      'message_name':forms.TextInput(attrs={'class':'form-controls'}),
      'message_email':forms.EmailInput(attrs={'class':'form-controls'}),
      'message_content':forms.Textarea(attrs={'class':'form-controls'}),
      'phoneNumber':forms.NumberInput(attrs={'class':'form-controls'}),
    }
    
# Creating booking form for client
class BookingForm(ModelForm):
  class Meta:
    model = Booking
    fields = "__all__"
    
    widgets = {
      'client_name':forms.TextInput(attrs={'class':'form-controls'}),
      'client_email':forms.EmailInput(attrs={'class':'form-controls'}),
      'client_content':forms.Textarea(attrs={'class':'form-controls'}),
      'client_phoneNumber':forms.NumberInput(attrs={'class':'form-controls'}),
    }