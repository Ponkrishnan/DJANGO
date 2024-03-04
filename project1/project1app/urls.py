from django.urls import path
from .views import *

urlpatterns=[
    path('',index,name='none'),
    path('index1/',index1,name='none'),
    path('index2/',index2,name='none'),
    path('index3/',index3,name='none'),
]
