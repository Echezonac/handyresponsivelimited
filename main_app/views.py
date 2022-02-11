from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from .models import *
from .forms import *
# Create your views here.
def home(request):
  booked = False
  if request.method == "POST":
    bookingform = BookingForm(request.POST)
    if bookingform.is_valid():
      bookingform.save()
      return HttpResponseRedirect('/home?booked=True')
  else:
    bookingform = BookingForm
    if 'booked' in request.GET:
      booked = True
  context={
    'bookingform':bookingform,
    'booked':booked,
    'Carousels':Hero.objects.all(),
    'Abouts':About.objects.all(),
    'Services':Service.objects.all(),
    'Testimonies':Testimony.objects.all(),
    # 'news':news_list
  }
  return render(request,'pages/index.html',context)

class ServiceDetail(DetailView):
  model = Service
  template_name = 'pages/service-detail.html'
  
class BlogDetail(DetailView):
  model = News
  template_name = 'pages/blog-detail.html'

def more(request):
  return render(request,'pages/about.html',{})

def contact(request):
  submitted = False
  if request.method == "POST":
    form = MessageForm(request.POST)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/contact?submitted=True')
  else:
    form = MessageForm
    if 'submitted' in request.GET:
      submitted = True
  context ={
    'form':form,
    'submitted':submitted,
    'contacts':Contact.objects.all(),
    'maps':LocationMAp.objects.all(),
    'addresses':Address.objects.all(),
    'icons':Social_Links.objects.all()
  }
  return render(request,'pages/contact.html',context)
  
def dashboard(request):
  context = {
    'client_requests':Booking.objects.all().order_by('-id'),
  }
  return render(request,'pages/bookings.html',context)

def messages(request):
  context = {
    'message_lists':Message.objects.all().order_by('-id'),
  }
  return render(request,'pages/messages.html',context)
