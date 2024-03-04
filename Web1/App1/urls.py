from os import path
from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='index'),
    path('p1/',p1,name='index'),
    path('p2/',p2,name='index'),
    path('p3/',p3,name='index'),
    path('1/',index2,name='index2'),
    path('home/',home,name='home')
] 