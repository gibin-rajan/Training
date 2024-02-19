from SampleApp import views
from django.urls import path


urlpatterns=[
    path('',views.frst,name='frst'),
    path('sc',views.scnd,name='scnd'),
    path('th',views.thrd,name='thd'),
    path('tp',views.temp,name='temp'),
    path('dtl',views.dtl,name='dtl'),
    path('tp1',views.temp1,name='temp1')
    ]