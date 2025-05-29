from django.urls import path
from coures.views import django,python

urlpatterns = [
    path('dj/',django),
    path('py/',python),
]
