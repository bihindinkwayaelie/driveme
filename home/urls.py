import imp 
from xml.dom.minidom import Document
from django.urls import path
from .import views                      
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index, name='welcome'),
    path('dashboard/',views.dashboard, name='dashboard'),
    path('dashboard2/',views.dashboard2, name='dashboard2'),
    path('signin/',views.signin, name='signin'),
    path('monday/',views.monday, name='monday'),
    path('contact/',views.contact, name='contact'),
    path('signup/',views.signup, name='signup'),
    path('base/',views.base, name='base'),
    path('services/',views.services, name='services'),
    path('requestdriver/',views.requestdriver, name='requestdriver'),
    path('more/<int:id>',views.more, name='more'),
    path('approveddrivers/',views.approveddrivers, name='approveddrivers')
    ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)