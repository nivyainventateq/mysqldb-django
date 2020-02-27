from django.urls import path,include
from myappdb.views import test

urlpatterns = [
    path('site/', view=test, name='test'),
]


