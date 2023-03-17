from app.views import *

from django.urls import path
app_name='app'
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('dhoni/',dhoni,name='dhoni'),
]