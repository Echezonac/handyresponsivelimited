from django.urls import path
from .views import *

urlpatterns = [
  path('',home, name='home_page'),
  path('home/',home, name='home_page'),
  path('pagn/',pagn, name='pagn_page'),
  path('more/',more, name='more_page'),
  path('contact/',contact, name='contact_page'),
  path('admin_dashboard/',dashboard, name='admin_page'),
  path('admin_messages/',messages, name='messages_page'),
  path('detail/<int:pk>',ServiceDetail.as_view(), name="detail_page"),
  path('detailBlog/<int:pk>',BlogDetail.as_view(), name="detail_blog_page"),
]
