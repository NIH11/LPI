from django.contrib import admin
from django.urls import path
from Home import views

urlpatterns = [
    path('',views.index, name='Home'),
    path('calculator',views.calculator, name='calculator'),
    path('Services',views.services, name='Services'),
    path('Aboutus',views.Aboutus, name='Aboutus'),
    path('Contactus',views.Contactus, name='Contactus'),
    path('LPI',views.LPI, name='LPI'),
    path('lpiorganic',views.lpiorganic, name='lpiorganic'),
    path('lpiinorganic',views.lpiinorganic, name='lpiinorganic'),
    path('lpiheavymetals',views.lpiheavymetals, name='lpiheavymetals'),
    
            
]