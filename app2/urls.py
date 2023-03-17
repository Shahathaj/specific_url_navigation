from app2.views import *
from django.urls import path
app_name='app2'
urlpatterns=[
    path('naveenkumar/',naveenkumar,name='naveenkumar'),
    path('pradeepnarwal/',pradeepnarwal,name='pradeepnarwal'),
]